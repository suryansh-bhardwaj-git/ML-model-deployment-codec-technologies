Cloud-Based Machine Learning Model Deployment

Overview

This project demonstrates how a Machine Learning model can be deployed as a cloud-based REST API. The application uses the Iris Flower Dataset and predicts the flower species based on user input.

The model is trained using Scikit-Learn and served through a Flask API. Once deployed to the cloud, users can access the prediction service from anywhere using an internet connection.


Technologies Used

- Python
- Flask
- Scikit-Learn
- Joblib
- Render / AWS


How It Works

1. Load the Iris dataset.
2. Train a Random Forest Classifier model.
3. Save the trained model.
4. Create a Flask API.
5. Send flower measurements to the API.
6. Receive the predicted flower species.


Project Structure

cloud-ml-project/
│
├── app.py
├── requirements.txt
└── README.md


Running the Project

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

The API will start on:

http://localhost:5000


API Endpoint

Predict Flower Species

POST "/predict"

Sample Input:

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

Sample Output:

{
  "prediction": "Setosa"
}


Deployment

The project can be deployed on cloud platforms such as Render, Railway, AWS, or Azure. After deployment, the API can be accessed through a public URL.


Conclusion

This project shows a simple example of deploying a Machine Learning model as a cloud service. It helps understand the basic concepts of machine learning, APIs, and cloud deployment.