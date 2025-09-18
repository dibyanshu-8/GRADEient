# GRADEient: Student Performance Prediction Web App

GRADEient is a machine learning web application built with Flask that predicts a student's grade classification based on various demographic, academic, and lifestyle factors. This project showcases a complete data science workflow, from data analysis and model training to a final, containerized application deployed on the cloud.

## Features

* **Predictive Model**: Utilizes a trained Scikit-learn machine learning model to classify student performance into distinct grade brackets.
* **Interactive Web Interface**: A user-friendly web form, built with Flask and HTML/CSS, allows for the input of student data to receive a real-time prediction.
* **Data Preprocessing Pipeline**: Implements a data preprocessing pipeline (using `pickle`) that handles categorical and numerical features to prepare user input for the model.
* **End-to-End Workflow**: Demonstrates the full process of a data science project, from analysis in a Jupyter Notebook to a deployed web application.

## Technology Stack & Libraries

* **Backend**: Python, Flask
* **Data Science/ML**: Scikit-learn, Pandas, NumPy
* **Frontend**: HTML, CSS
* **Containerization**: Docker
* **Deployment**: Gunicorn, Microsoft Azure

## Local Setup Instructions

You can run this project locally using either Docker (recommended for consistency) or a standard Python virtual environment.

### Running with Docker (Recommended)

This method ensures the application runs in a clean, isolated environment.

1.  **Prerequisites**: Git, Docker Desktop.
2.  **Clone the repository:**
    ```sh
    git clone [https://github.com/dibyanshu-8/GRADEient.git](https://github.com/dibyanshu-8/GRADEient.git)
    ```
3.  **Navigate to the project directory:**
    ```sh
    cd GRADEient
    ```
4.  **Build the Docker image:**
    ```sh
    docker build -t gradient-app .
    ```
5.  **Run the Docker container:**
    ```sh
    docker run -p 5000:5000 gradient-app
    ```
6.  **Access the application** in your browser at [http://localhost:5000/](http://localhost:5000/).

### Running Locally (Without Docker)

1.  **Prerequisites**: Git, Python 3.8+.
2.  **Clone the repository:**
    ```sh
    git clone [https://github.com/dibyanshu-8/GRADEient.git](https://github.com/dibyanshu-8/GRADEient.git)
    ```
3.  **Navigate to the project directory and create a virtual environment:**
    ```sh
    cd GRADEient
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
5.  **Run the Flask application:**
    ```sh
    python app.py
    ```
6.  **Access the application** in your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Deployment

This application has been successfully containerized with Docker and deployed to **Microsoft Azure App Service**, demonstrating a scalable and production-ready setup.