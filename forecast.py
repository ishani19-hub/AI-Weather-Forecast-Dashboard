import requests
import os
from dotenv import load_dotenv


load_dotenv()


API_KEY=os.getenv("WEATHER_API_KEY")


BASE_URL="https://api.weatherapi.com/v1/forecast.json"



def get_forecast(city,days=3):


    try:


        url=(

            f"{BASE_URL}"
            f"?key={API_KEY}"
            f"&q={city}"
            f"&days={days}"

        )



        response=requests.get(
            url,
            timeout=10
        )



        data=response.json()



        if "error" in data:

            return None




        result=[]



        for item in data["forecast"]["forecastday"]:



            day=item["day"]

            astro=item["astro"]




            icon=day["condition"]["icon"]


            if icon.startswith("//"):

                icon="https:"+icon





            result.append({



                "date":
                item["date"],



                "max_temp":
                day["maxtemp_c"],



                "avg_temp":
                day["avgtemp_c"],



                "min_temp":
                day["mintemp_c"],



                "temperature":
                day["avgtemp_c"],



                "condition":
                day["condition"]["text"],



                "icon":
                icon,



                "rain_probability":
                day.get(
                    "daily_chance_of_rain",
                    0
                ),



                "sunrise":
                astro.get(
                    "sunrise",
                    "N/A"
                ),



                "sunset":
                astro.get(
                    "sunset",
                    "N/A"
                ),



                "moon_phase":
                astro.get(
                    "moon_phase",
                    "N/A"
                )


            })



        return result



    except Exception as e:


        print(
            "Forecast Error:",
            e
        )


        return None