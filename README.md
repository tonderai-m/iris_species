
# Data Science Project: Best Linear Predictor (BLP) with Front-End Interface

This project demonstrates how to build a **Best Linear Predictor (BLP)** model for predictive data science analysis on the **Iris dataset** and integrate it with a user-friendly front-end interface for real-time interaction.

The project includes:
1. **Data Science Component**: A predictive model built using the Best Linear Predictor (BLP) approach applied to the Iris dataset.
2. **Front-End Interface**: An interactive web interface where users can input data and view the prediction result from the model.
3. **Back-End API**: A Flask-based API that hosts the model and interacts with the front-end.

## Project Overview

This project applies the **Best Linear Predictor (BLP)** method to predict the species of iris flowers based on four input features. The model is implemented in Python and Flask, while the front-end uses HTML and JavaScript for user interaction.

### Key Components:
1. **Best Linear Predictor (BLP) Model**: 
    - The model is implemented to predict the species of iris flowers using the BLP approach.
    - Features: `sepal_length`, `sepal_width`, `petal_length`, `petal_width`.
    - Target: `species` (setosa, versicolor, virginica).
2. **Front-End Interface**: 
    - The user inputs relevant data through an HTML form (sepal and petal measurements). 
    - The data is then sent to the Flask back-end, which applies the BLP model and returns the predicted species.
3. **Back-End API (Flask)**: 
    - The Flask API receives the input data, processes it using the BLP model, and sends back the prediction result.
    - The API also handles requests from the front-end in a JSON format.

## Iris Dataset Overview

The **Iris dataset**, introduced by the famous statistician and biologist **Ronald A. Fisher** in 1936, is one of the most well-known datasets in machine learning and statistics. It consists of 150 samples from three different species of iris flowers: *Setosa*, *Versicolor*, and *Virginica*. 

### Features:
1. **Sepal Length** (cm)
2. **Sepal Width** (cm)
3. **Petal Length** (cm)
4. **Petal Width** (cm)

### Target:
- The target variable is the **species** of the iris flower, which can be one of the following:
  - *Setosa*
  - *Versicolor*
  - *Virginica*

### Purpose:
The goal of using the Iris dataset is to classify the species of the iris flowers based on their sepal and petal dimensions. It is often used for classification and clustering tasks in data science, as well as for model evaluation purposes.

The **Best Linear Predictor (BLP)** model is applied here to predict the species of the iris flowers using a linear approach to minimize prediction errors based on the input features.

## Technologies Used

- **Data Science**: Python, NumPy, Pandas, Scikit-learn (for linear regression and model evaluation)
- **Back-End**: Python, Flask (for creating the RESTful API)
- **Front-End**: HTML, JavaScript (with Fetch API for making requests to the back-end)
- **Deployment**: GitHub Pages (for front-end), Render/Heroku (for back-end)

## Getting Started

To get this project up and running on your local machine or deploy it to your hosting environment, follow the steps below.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Setting Up the Front-End
The front-end is located in the `frontend/` directory. Open the `index.html` file in a browser to view it. You can modify the HTML file to suit your needs for the data input.

### 3. Setting Up the Back-End (Flask)
The back-end is located in the `backend/` directory. To run the Flask app locally:
1. Set up a Python virtual environment:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   pip install -r requirements.txt
   ```
2. Run the Flask app:
   ```bash
   python app.py  # Starts the Flask server
   ```

The Flask API will now be running locally on `http://127.0.0.1:5000` or the port you've configured.

### 4. Update the Front-End to Point to Your API
In your front-end `index.html` file, update the fetch URL to match your API endpoint:
```javascript
const response = await fetch("http://127.0.0.1:5000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ sepal_length: value1, sepal_width: value2, petal_length: value3, petal_width: value4 })
});
```

### 5. Deploying the Application
#### Front-End (GitHub Pages)
1. Push your front-end code to GitHub.
2. In the GitHub repository settings, under the **GitHub Pages** section, set the source branch to `main` and folder to `/ (root)`.
3. GitHub Pages will generate a URL (e.g., `https://yourusername.github.io/your-repo`).

#### Back-End (Render/Heroku)
1. Deploy the Flask app to a cloud platform like **Render** or **Heroku**.
2. Update the front-end to use the deployed back-end URL (e.g., `https://your-app.onrender.com`).

## API Endpoints

### POST `/predict`
- **URL**: `/predict`
- **Method**: `POST`
- **Request Body** (JSON format):
  ```json
  {
    "sepal_length": <value1>,
    "sepal_width": <value2>,
    "petal_length": <value3>,
    "petal_width": <value4>
  }
  ```
- **Response** (JSON format):
  ```json
  {
    "prediction": "setosa"
  }
  ```

## Example Workflow

1. The user enters sepal and petal measurements in the front-end form.
2. The front-end sends the feature values to the back-end via a POST request.
3. The Flask back-end processes the data using the BLP model and returns the predicted species.
4. The front-end dynamically displays the prediction result to the user.

## Data Science Model: Best Linear Predictor (BLP)

The **Best Linear Predictor (BLP)** is a linear regression model that predicts the value of the dependent variable by minimizing the error in the predictions based on the provided features.

### Steps Taken to Build the BLP Model:
1. **Data Preprocessing**: The Iris dataset is cleaned and prepared for training the model.
2. **Feature Selection**: The four features—sepal length, sepal width, petal length, and petal width—are used for prediction.
3. **Model Training**: The linear regression model is trained on the data to minimize the error.
4. **Model Evaluation**: The performance of the model is evaluated using metrics like R², Mean Squared Error (MSE), or similar.
5. **Prediction**: The trained model is used to make predictions based on new input data.

### Code Snippet for BLP Model:
```python
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target (species)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
blp_model = LinearRegression()
blp_model.fit(X_train, y_train)

# Make predictions
predictions = blp_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
```

## Contributing

If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your fork (`git push origin feature/your-feature`).
6. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

