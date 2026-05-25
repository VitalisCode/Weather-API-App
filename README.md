# Weather API App

A simple command-line application that fetches and displays current weather information for any city using the WeatherAPI.com API.

## Features

- Get real-time weather data for any city
- Display temperature, humidity, wind speed, and conditions
- Automatically save weather reports to a log file
- Error handling for invalid cities and network issues

## Requirements

- Python 3.x
- requests library
- WeatherAPI.com API key (free tier available)

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install requests
   ```
3. Obtain a free API key from [WeatherAPI.com](https://www.weatherapi.com/)

## Setup

Set your API key as an environment variable:
```
export WEATHER_API_KEY="your_api_key_here"
```

## Usage

Run the application:
```
python weather_app.py
```

Enter a city name when prompted. The application will display the current weather and save the report to `weather_logs.txt`.

Type 'quit' to exit the application.

## Output

Weather reports include:
- City and country
- Current temperature (Celsius)
- Weather condition
- Humidity percentage
- Wind speed (km/h)