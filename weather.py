import requests
import streamlit as st
def fetch_weather_data(api_key, city):
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(base_url)
    data = response.json()
    return data
def main():
    st.title("Weather App")

    api_key = "f44db17c82ec4bd5a6e171954230507" 
    city = st.text_input("Enter a city name")

    if st.button("Get Weather"):
        weather_data = fetch_weather_data(api_key, city)
        if "error" not in weather_data:
            current_condition = weather_data["current"]["condition"]["text"]
            temperature = weather_data["current"]["temp_c"]
            humidity = weather_data["current"]["humidity"]
            st.write(f"Weather in {city}: {current_condition}")
            st.write(f"Temperature: {temperature}°C")
            st.write(f"Humidity: {humidity}%")
        else:
            st.write(f"Error: {weather_data['error']['message']}")
if __name__ == "__main__":
    main()
