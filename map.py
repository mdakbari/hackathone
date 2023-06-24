import requests
import json
import datetime
import folium as fl
from streamlit_folium import st_folium
import streamlit as st





def get_weather_forecast(lat,longi):
    api_key = '30d4741c779ba94c470ca1f63045390a'  # Replace with your OpenWeatherMap API key

    # Construct the API request URL with the city name and API key
    geo_cordinats = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={longi}&appid={api_key}"


    response = requests.get(geo_cordinats)
    data = response.json()

    city_name = data['name']
    time = data['dt']
    datetime_obj = datetime.datetime.fromtimestamp(time)
    formatted_time = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

    weather = data['weather'][0]['main']
    temperature = data['main']['temp']
    real_feel = data['main']['feels_like']
    humidity = data['main']['humidity']

    return city_name, formatted_time, weather, temperature, real_feel, humidity





m = fl.Map()
m.add_child(fl.LatLngPopup())
map = st_folium(m, height=400, width=800)
button_clicked = st.button("Get Selected Place")

if button_clicked:
    data=[]
    try:
        data.append(map['last_clicked']['lat'])
        data.append(map['last_clicked']['lng'])
        if data is not None:
            city_name, time, weather, temperature, real_feel, humidity = get_weather_forecast(data[0],data[1])
            st.write("City Name:", city_name)
            st.write("Time:", time)
            st.write("Weather:", weather)
            st.write("Temperature:", temperature)
            st.write("Real Feel:", real_feel)
            st.write("Humidity:", humidity)
    except:
        pass