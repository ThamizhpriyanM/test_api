# Flask Weather App

This is a simple weather application built with Flask, allowing users to register, login, and check the weather for various cities.

## Features

- **User Authentication**: Users can register, login, and logout securely.
- **Weather Information**: Users can enter the name of a city and get the current weather conditions.

## Technologies Used

- **Flask**: Python web framework used for backend development.
- **SQLite**: Lightweight database management system for storing user information.
- **WTForms**: Form validation and rendering library for Flask.
- **bcrypt**: Password hashing library for securely storing passwords.
- **OpenWeatherMap API**: External API used to retrieve weather information based on user input.
- **HTML/CSS/JavaScript**: Frontend technologies for user interface and interactivity.

## Installation

1. Clone this repository:https://github.com/ThamizhpriyanM/test_api/tree/main

2. Navigate to the project directory:


3. Install the required dependencies:


4. Run the Flask application:


5. Open a web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

- **Registration**: Click on the "Register" link to create a new account. Enter a unique username and a strong password.
- **Login**: After registration, you can login with your credentials.
- **Weather Check**: Once logged in, you will be redirected to the weather page. Enter the name of a city and click "Get Weather" to see the current weather conditions.
- **Logout**: Click on the "Logout" link to log out of your account.
## Files
### Python (main.py file)

- **main.py**: Contains the Flask application and routes.

### HTML (templates folder)

- **home.html**: Homepage of the application.
- **login.html**: Login page.
- **dashboard.html**: Dashboard page after login.
- **register.html**: Registration page.
- **weather.html**: Weather page to display weather information.


