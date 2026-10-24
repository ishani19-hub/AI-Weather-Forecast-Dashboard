import requests
import os
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("WEATHER_API_KEY")


BASE_URL = "https://api.weatherapi.com/v1/current.json"


def get_air_quality(city):

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


        air = data["current"]["air_quality"]


        return {

            "pm25": round(air["pm2_5"],2),
            "pm10": round(air["pm10"],2),
            "co": round(air["co"],2),
            "no2": round(air["no2"],2),
            "so2": round(air["so2"],2),
            "o3": round(air["o3"],2)

        }


    except Exception as e:

        print("AQI Error:",e)

        return None