import requests
def get_location(city):
  url = "https://geocoding-api.open-meteo.com/v1/search"
  params={
    "name": city,
    "count": 1
  }
  response = requests.get(url , params=params)
  data=response.json()
  if "results" not in data:
        return None
  location=data["results"][0]
  return location

def get_weather(latitude, longitude):
 weather_url = "https://api.open-meteo.com/v1/forecast"
 weather_params={
    "latitude":latitude,
    "longitude":longitude,
    "current":"temperature_2m,relative_humidity_2m,wind_speed_10m"
 }
 weather_response=requests.get(weather_url , params=weather_params)
 weather_data=weather_response.json()
 return weather_data

city = input("Enter city name: ")

location = get_location(city)

if location:

    weather = get_weather(
        location["latitude"],
        location["longitude"]
    )

    print(" City:", location["name"])
    print(" Temperature:", weather["current"]["temperature_2m"], "°C")
    print(" Humidity:", weather["current"]["relative_humidity_2m"], "%")
    print(" Wind Speed:", weather["current"]["wind_speed_10m"], "km/h")

else:
    print(" City not found!")
