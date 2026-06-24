Cloud-Based Machine Learning Model Deployment

Overview

This project demonstrates the deployment of a Machine Learning model as a cloud-hosted REST API. The application uses the Iris Flower Dataset and predicts the flower species based on the input measurements provided by the user.

The model is built using Scikit-Learn and deployed using Flask on Render Cloud.

Technologies Used

- Python
- Flask
- Scikit-Learn
- Joblib
- Render

Live Demo

https://ml-model-deployment-codec-technologies.onrender.com

Features

- Machine Learning model deployment
- REST API for predictions
- Cloud hosting using Render
- Simple and beginner-friendly implementation

Project Structure

ML-model-deployment-codec-technologies/
│
├── app.py
├── requirements.txt
└── README.md

API Endpoint

Home

GET /

Response:

{
  "project": "Cloud-Based ML Model Deployment",
  "status": "Running"
}

Conclusion

This project demonstrates the basic process of training, deploying, and hosting a Machine Learning model on the cloud. The deployed API can be accessed from anywhere using its public URL.