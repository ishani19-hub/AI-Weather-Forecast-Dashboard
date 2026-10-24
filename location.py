import requests


def get_location():

    try:

        # Primary location API
        response = requests.get(
            "https://ipapi.co/json/",
            timeout=10
        )

        data = response.json()


        city = data.get("city")
        country = data.get("country_name")


        # If API fails, use another API
        if not city or not country:


            response = requests.get(
                "https://ipinfo.io/json",
                timeout=10
            )


            data = response.json()


            city = data.get("city")
            country = data.get("country")



        return {

            "city": city if city else "Unknown",

            "country": country if country else "Unknown"

        }



    except Exception as e:


        print(
            "Location Error:",
            e
        )


        return {

            "city":"Unknown",

            "country":"Unknown"

        }