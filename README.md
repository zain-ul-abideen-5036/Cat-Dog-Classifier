# Cat/Dog Image Classifier
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-brightgreen)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)

A deep learning-powered web application that classifies images of cats and dogs using TensorFlow and Flask.

<img width="503" alt="image" src="https://github.com/user-attachments/assets/d31922c0-8153-404d-b117-9b0776a7e38e" />

---

## Features
- Web interface for image upload
- Real-time predictions using MobileNetV2 transfer learning
- Responsive UI with loading states
- Error handling and file validation
---

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

1. Clone repository
```bash
git clone https://github.com/zain-ul-abideen-5036/Cat-Dog-Classifier.git
cd Cat-Dog-Classifier
```

2. Install dependencies
```
pip install -r requirements.txt
```
---

## Usage

### Model Training
1. Run the Jupyter notebook:
```
jupyter notebook notebooks/HandwrittenDigitClassification.ipnyb
```
2. Execute all cells to:
    - Load and visualize data.
    - Train the model.

### Start Web Server
```bash
python app.py
```
Access the web interface at ```http://localhost:5000```

---

## Project Structure
```
Cat-Dog-Classifier/
├── static/
│   ├── styles.css           # Frontend styles
│   └── uploads/             # Uploaded images (auto-created)
├── templates/
│   └── index.html           # Main UI
├── train.ipynb              # Colab training notebook
├── app.py                   # Flask backend
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```
---

## Tech Stack
- **Backend:** TensorFlow 2.16.1, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Model:** MobileNetV2 transfer learning
---

## Contributing
- Fork the repository
- Create feature branch
- Submit PR with detailed description
---

## Contact
For questions or feedback, contact: abideen5036@gmail.com

---
