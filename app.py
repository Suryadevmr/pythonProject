from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "e8519707397081be8687f7d9e7472dac"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    if not city:
        return "Please provide a city name."

    # Fetch weather data
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        }
        return render_template("weather.html", weather=weather_data)
    else:
        return "City not found. Please try again."

if __name__ == "__main__":
    app.run(debug=True)
