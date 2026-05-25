import requests
import os
from datetime import datetime


API_KEY = os.getenv("WEATHER_API_KEY")


def save_weather_report(report):

    with open("weather_logs.txt", "a") as file:
        file.write(report + "\n")
        file.write("-" * 40 + "\n")


def get_weather(city):

    url = (
        f"http://api.weatherapi.com/v1/current.json"
        f"?key={API_KEY}&q={city}"
    )

    try:

        response = requests.get(url)

        data = response.json()

        # API error handling
        if "error" in data:
            print(f" Error: {data['error']['message']}")
            return

        city_name = data["location"]["name"]
        country = data["location"]["country"]

        temperature = data["current"]["temp_c"]

        condition = data["current"]["condition"]["text"]

        humidity = data["current"]["humidity"]

        wind_speed = data["current"]["wind_kph"]

        current_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        report = f"""
==========================
      WEATHER REPORT
==========================

Time: {current_time}
City: {city_name}
Country: {country}
Temperature: {temperature}°C
Condition: {condition}
Humidity: {humidity}%
Wind Speed: {wind_speed} kph
"""

        print(report)

        save_weather_report(report)

        print(" Report saved to weather_logs.txt\n")

    except requests.exceptions.RequestException as error:
        print(f" Network Error: {error}")


def main():

    print("=" * 40)
    print("        WEATHER API APP")
    print("=" * 40)

    while True:

        city = input(
            "\nEnter city name (or 'quit' to exit): "
        )

        if city.lower() == "quit":
            print("👋 Goodbye")
            break

        get_weather(city)


if __name__ == "__main__":
    main()