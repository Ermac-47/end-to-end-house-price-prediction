#  🏠 End-to-End House Price Prediction Using Machine Learning
📌 Project Overview

This project is an end-to-end machine learning application that predicts house prices based on key housing and neighborhood features. It includes a complete ML pipeline—from data ingestion and preprocessing to model training, evaluation, and deployment using a Flask web application.

🎯 Problem Statement

Accurately estimating house prices is critical for buyers, sellers, and real estate analysts. This project aims to build a machine learning model that predicts housing prices using structured data and serves predictions through a user-friendly web interface.

🧠 Solution Approach

Performed exploratory data analysis on housing data

Built a robust data preprocessing pipeline

Trained and evaluated multiple regression models

Selected the best-performing model

Saved trained artifacts for inference

Deployed prediction pipeline using Flask

🛠 Tech Stack

Programming Language: Python

Libraries: Pandas, NumPy, Scikit-learn, CatBoost, XGBoost

Web Framework: Flask

Tools: Git, GitHub

⚙️ Project Architecture
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipelines/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
├── templates/
│   ├── index.html
│   └── home.html
├── app.py
├── requirements.txt
└── README.md

📊 Model Training

Models evaluated: Linear Regression, Random Forest, Gradient Boosting, XGBoost, CatBoost

Evaluation metric: R² Score

Best-performing model was selected and saved for inference

Model training is performed offline using the training pipeline.
The deployed application loads pre-trained artifacts for prediction.

🌐 Web Application

Users can input housing feature values via a web form, and the application predicts the estimated house price in real time.

🚀 How to Run Locally
git clone <repo-url>
cd house-price-prediction
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python application.py

🔮 Future Improvements

Add model explainability (SHAP / feature importance)

Improve UI and input validation

Dockerize the application

Deploy on cloud (AWS / Render / Railway)