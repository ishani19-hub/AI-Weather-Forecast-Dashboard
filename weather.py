import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.weatherapi.com/v1/current.json"



def get_weather(city):

    try:

        url = (
            f"{BASE_URL}"
            f"?key={API_KEY}"
            f"&q={city}"
            f"&aqi=yes"
        )


        response = requests.get(
            url,
            timeout=10
        )


        data = response.json()


        if "error" in data:

            return None



        current = data["current"]

        location = data["location"]



        icon = current["condition"]["icon"]


        if icon.startswith("//"):

            icon = "https:" + icon



        air = current.get(
            "air_quality",
            {}
        )


        return {


            "city":
            location["name"],


            "country":
            location["country"],


            "time":
            location["localtime"],


            "temp":
            current["temp_c"],


            "feels":
            current["feelslike_c"],


            "humidity":
            current["humidity"],


            "wind":
            current["wind_kph"],


            "condition":
            current["condition"]["text"],


            "icon":
            icon,


            "visibility":
            current["vis_km"],


            "uv":
            current["uv"],



            "pm2_5":
            air.get("pm2_5","N/A"),


            "pm10":
            air.get("pm10","N/A"),


            "co":
            air.get("co","N/A"),


            "no2":
            air.get("no2","N/A"),


            "o3":
            air.get("o3","N/A")

        }


    except Exception as e:

        print("Weather Error:",e)

        return None