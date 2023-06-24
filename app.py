import requests
import json
import datetime

def get_data():
    # Prompt the user to enter a city name
    next = True
    while next:
        city = input("Enter a city name: ")

        if city:
            get_weather_forecast(city)
            next = False
        else:
            print("Please enter a valid input!")

def get_weather_forecast(city):
    api_key = '30d4741c779ba94c470ca1f63045390a'  # Replace with your OpenWeatherMap API key

    # Construct the API request URL with the city name and API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    try:
        # Send a GET request to the OpenWeatherMap API
        response = requests.get(url)
        country = get_info(city)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract relevant weather information
            weather = data["weather"][0]["main"]
            temperature = round(data["main"]["temp"])
            feels_like = round(data["main"]["feels_like"])
            celsius = round(fahrenheit_to_celsius(temperature))
            humidity = data["main"]["humidity"]

            current_datetime = datetime.datetime.now()
            current_date = current_datetime.date()
            current_hour = current_datetime.strftime("%I")
            current_minute = current_datetime.strftime("%M")
            am_pm = current_datetime.strftime("%p")

            print('\n')
            # Display the weather forecast
            print(f"Weather forecast for {city}:")
            print("Current time:", current_date, current_hour + ":" + current_minute + " " + am_pm)
            print(f"Weather: {weather}")
            print(f"Temperature: {temperature}°F", f" {celsius}°C")
            print(f"Real Feel: {feels_like}°F")
            print(f"Humidity: {humidity}%")
            if country:
                print(f'{city}, {country}')


        else:
            print("Failed to fetch weather data.")
            get_data()
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        get_data()


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def get_info(city):
    from geopy.geocoders import Nominatim

    # Create a geocoder instance
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Input city
    # city = "Ahmedabad"

    try:
        # Use geocoder to get the location details
        location = geolocator.geocode(city, exactly_one=True)
        parts = location.address.split(", ")
        country = parts[-1]
        return country
    except Exception as e:
        print("An error occurred:", e)
        return None


if __name__ == '__main__':
    get_data()
