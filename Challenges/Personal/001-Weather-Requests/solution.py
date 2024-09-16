# Personal Challenge - Weather Request

# Write a script to fetch the weather from the following cities
#
# Chicago, Sao Paulo, Mumbai, Tokio, Toronto
#
# and store the city and weather in a dictionary. 

# You can use any free api available online
import os
from dotenv import load_dotenv, dotenv_values
import requests

load_dotenv() # Used to not expose my key to the repository

def RetrieveCurrentWeather(data: dict) -> str:
    return data['current']["condition"]["text"]

def GetCityWeather(city: str) -> str:
    key = os.getenv("WEATHER_API_KEY")
    baseUrl = "http://api.weatherapi.com/v1"
    endpoint = "/current.json"
    parameters = { 
        "key": key,
        "q": city
        }
    url = baseUrl + endpoint

    r = requests.get(url, timeout=3, params=parameters)

    if r.status_code == 200:
       return RetrieveCurrentWeather(r.json())
    else:
        print(f"Request to {url} failed with code {r.status_code}")
        return ""

cities = ["Chicago", "Sao Paulo", "Mumbai", "Tokio", "Toronto"]

result = dict()
for city in cities:
    result[city] = GetCityWeather(city)

print(result)