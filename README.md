# iris_species
# Front-End and Back-End Integration Example

This project demonstrates how to create a simple front-end that communicates with a back-end API deployed using Flask. The project uses a web interface for users to input data, which is then sent to the Flask back-end to process and return a result.

## Project Overview

The project consists of two main parts:
1. **Front-End**: A simple HTML page with an input form that collects data from the user.
2. **Back-End**: A Flask API that processes the data and returns a result (e.g., simple addition of numbers or prediction from a model).

### Front-End
- The front-end is a basic HTML form that collects two numbers from the user.
- It communicates with the back-end using JavaScript's `fetch()` function to send a POST request to the Flask API.
- The result from the API is displayed dynamically on the front-end without needing to reload the page.

### Back-End
- The back-end is a Flask application deployed on a hosting platform like **Render**.
- The back-end receives a JSON payload with two numbers (or data) from the front-end, processes them, and sends back a response with the result.

## Technologies Used

- **Front-End**: HTML, CSS (for basic styling), JavaScript (for asynchronous communication)
- **Back-End**: Python, Flask (for the API)
- **Deployment**: GitHub Pages (for front-end), Render (for back-end)

## Getting Started

To get this project up and running on your local machine or deploy it to your own hosting environment, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo

