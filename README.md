# Celebrity Image Classifier

A machine learning–based web application that identifies celebrities from uploaded images. The application uses **OpenCV** for face and eye detection, **Wavelet Transform** for feature extraction, and a trained **Machine Learning classification model** to predict the celebrity.

The application is served using a **Flask backend** and deployed on an **AWS EC2 instance with Nginx**.

## 🚀 Features

* Upload an image through a web interface
* Automatically detects faces using OpenCV
* Detects eyes to filter valid facial images
* Extracts facial features using Wavelet Transform
* Classifies the detected face using a trained ML model
* Displays the predicted celebrity and classification scores
* Flask REST API connects the ML model with the frontend
* Deployed on AWS EC2 with Nginx

## 🛠️ Tech Stack

**Machine Learning**

* Python
* Scikit-learn
* NumPy
* PyWavelets

**Computer Vision**

* OpenCV
* Haar Cascade Classifiers

**Backend**

* Flask

**Frontend**

* HTML
* CSS
* JavaScript

**Deployment**

* AWS EC2
* Nginx

## ⚙️ How It Works

The classification pipeline follows these steps:

**1. Image Upload**

The user uploads an image through the web interface.

**2. Face Detection**

OpenCV's Haar Cascade classifier detects faces in the uploaded image.

**3. Eye Detection**

The detected face is checked for visible eyes. Images with a valid face and at least two detected eyes are used for classification.

**4. Image Preprocessing**

The detected face is cropped and resized before being passed to the machine learning model.

**5. Feature Extraction**

Wavelet Transform is applied to the cropped facial image to extract important facial features such as edges and structural information.

The raw image features and wavelet features are combined to create the final feature vector.

**6. Classification**

The processed feature vector is passed to the trained machine learning model, which predicts the celebrity.

**7. Result**

The predicted celebrity and corresponding classification probabilities/scores are returned by the Flask API and displayed on the website.

## 📂 Project Structure

```text
Celebrity-Image-Classifier/
│
├── UI/
│   ├── app.html
│   ├── app.css
│   ├── app.js
│   └── images/
│
├── server/
│   ├── server.py
│   ├── util.py
│   └── artifacts/
│
├── model/
│   ├── opencv/
│   │   ├── haarcascade_frontalface_default.xml
│   │   └── haarcascade_eye.xml
│   │
│   └── telugu_celeb.ipynb
│
├── requirements.txt
└── README.md
```

> The exact structure may vary depending on the repository version.

## 🧠 Machine Learning Pipeline

```text
Input Image
     ↓
Face Detection
     ↓
Eye Detection
     ↓
Face Cropping
     ↓
Image Resizing
     ↓
Wavelet Transform
     ↓
Feature Extraction
     ↓
Trained ML Classifier
     ↓
Celebrity Prediction
```
