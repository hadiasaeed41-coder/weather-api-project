import requests
def get_location(city):
  url = "https://geocoding-api.open-meteo.com/v1/search"
  params={
    "name": city,
    "count": 1
  }
  try:
   response = requests.get(url , params=params)
   data=response.json()
   if "results" not in data:
        return None
   location=data["results"][0]
   return location
  except:
   return None

def get_weather(latitude, longitude):
 weather_url = "https://api.open-meteo.com/v1/forecast"
 weather_params={
    "latitude":latitude,
    "longitude":longitude,
    "current":"temperature_2m,relative_humidity_2m,wind_speed_10m"
 }
 try:
  weather_response=requests.get(weather_url , params=weather_params)
  weather_data=weather_response.json()
  return weather_data
 except:
  return None
while True: 
 city = input("Enter city name: ")
 if city =="":
  print("please enter city name")
  continue
 location = get_location(city)

 if location:

    weather = get_weather(
        location["latitude"],
        location["longitude"]
    )
    if weather:
     print("\n------ Weather Report ------")
     print("City:", location["name"])
     print("Country:", location["country"])
     print("Temperature:", weather["current"]["temperature_2m"], "°C")
     print("Humidity:", weather["current"]["relative_humidity_2m"], "%")
     print("Wind Speed:", weather["current"]["wind_speed_10m"], "km/h")
     print("----------------------------")
    else:
      print("Weather not available")
 else:
    print(" City not found!")



 again = input("\nSearch another city? (yes/no): ")
 if again.lower() != "yes":
    print("Thank you!")
    break
 