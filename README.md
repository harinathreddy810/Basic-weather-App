Project Title: Basic Weather Application using Flask

Project Description:
This project is a Basic Weather Application built with Python’s Flask web framework. It fetches and displays real-time weather data from the OpenWeatherMap API based on user-provided city names or ZIP codes. This application allows users to quickly access current weather information, including temperature, weather description, humidity, and wind speed, in a user-friendly web interface.

Key Components:

Backend (Python with Flask):

The backend is implemented using Flask, serving as a lightweight web server.
The application receives user input (location) via a form, processes the request, and retrieves weather data from the OpenWeatherMap API using the requests library.
The get_weather_data function makes an HTTP request to the API, handling any exceptions and returning JSON data if successful.

API Integration:

OpenWeatherMap API is used to obtain current weather data, accessed using an API key and queried by location.
Temperature, humidity, weather description, and wind speed are extracted and displayed.

Frontend (HTML, CSS):

HTML (index.html): A clean, structured interface allowing users to input their city name or ZIP code. It includes placeholders for dynamic weather information that updates when the data is available.
CSS (style.css): The application is styled for a modern, minimalistic look. The layout is centered with form controls, weather data display sections, and icons for temperature and weather conditions.
Features:

Location-based Weather Display: Users can enter any city or ZIP code to get instant weather updates.
Weather Details: Displays temperature, weather description, humidity, and wind speed.
Dynamic Error Handling: If the location is invalid or data is unavailable, users receive a notification.

Usage:

Run the application by executing the Flask server. Access the app via localhost, enter the desired location, and view updated weather data.
This project provides an excellent introduction to Flask, APIs, and dynamic web application development while creating a practical and user-friendly weather app.
