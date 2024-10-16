from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual OpenWeatherMap API key
API_KEY = "ed23aa11c87df01c2fa8650485810caa"

# Function to fetch weather data
def get_weather_data(location, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Exception occurred: {e}")
        return None

# Main route for the web app
@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        location = request.form.get("location").strip()
        if location:
            weather_data = get_weather_data(location, API_KEY)
    
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
