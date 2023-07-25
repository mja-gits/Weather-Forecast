# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 01:51:57 2023

@author: MJA
"""

import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_weather_temperature(data, target_date):
    for forecast in data["list"]:
        if forecast["dt_txt"] == target_date:
            return forecast["main"]["temp"]
    return None

def get_wind_speed(data, target_date):
    for forecast in data["list"]:
        if forecast["dt_txt"] == target_date:
            return forecast["wind"]["speed"]
    return None

def get_pressure(data, target_date):
    for forecast in data["list"]:
        if forecast["dt_txt"] == target_date:
            return forecast["main"]["pressure"]
    return None

def main():
    data = get_weather_data()
    if not data:
        return

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            target_date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temperature = get_weather_temperature(data, target_date)
            if temperature:
                print(f"The temperature on {target_date} is {temperature} Kelvin.")
            else:
                print("Data not found for the given date.")
        elif choice == 2:
            target_date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed(data, target_date)
            if wind_speed:
                print(f"The wind speed on {target_date} is {wind_speed} m/s.")
            else:
                print("Data not found for the given date.")
        elif choice == 3:
            target_date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure(data, target_date)
            if pressure:
                print(f"The pressure on {target_date} is {pressure} hPa.")
            else:
                print("Data not found for the given date.")
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
