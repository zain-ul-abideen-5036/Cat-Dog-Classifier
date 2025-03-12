from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import os
import tensorflow as tf
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB limit
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Load model with error handling
try:
    model = load_model('cats_dogs_model.keras')
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'})
    
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'})
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type'})

        # Create directories if missing
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)

        # Process image
        img = tf.keras.utils.load_img(save_path, target_size=(150, 150))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Predict
        prediction = model.predict(img_array)
        result = "Dog" if prediction > 0.5 else "Cat"

        return jsonify({
            'prediction': result,
            'image_url': f'uploads/{filename}'
        })
        
    except Exception as e:
        app.logger.error(f"Prediction error: {str(e)}")
        return jsonify({'error': 'Failed to process image'})

if __name__ == '__main__':
    app.run(debug=True)