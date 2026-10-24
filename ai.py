import os
from dotenv import load_dotenv
from google import genai

# =====================================
# LOAD ENVIRONMENT VARIABLES
# =====================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    client = genai.Client(api_key=API_KEY)
else:
    client = None


# =====================================
# AVAILABLE MODELS (Fallback Order)
# =====================================

MODELS = [
    "gemini-flash-lite-latest",
    "gemini-3.1-flash-lite",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
]


# =====================================
# WEATHER AI
# =====================================

def ask_weather_ai(question, weather_data):

    if not API_KEY:
        return "❌ Gemini API key not found. Please add GEMINI_API_KEY to your .env file."

    prompt = f"""
You are a friendly and intelligent weather assistant.

Current Weather

City: {weather_data.get('city', 'Unknown')}
Temperature: {weather_data.get('temperature', 'N/A')} °C
Condition: {weather_data.get('condition', 'N/A')}
Humidity: {weather_data.get('humidity', 'N/A')} %
Wind Speed: {weather_data.get('wind', 'N/A')} km/h
UV Index: {weather_data.get('uv', 'N/A')}
Chance of Rain: {weather_data.get('rain_probability', 'N/A')} %
Maximum Temperature: {weather_data.get('max_temp', 'N/A')} °C
Minimum Temperature: {weather_data.get('min_temp', 'N/A')} °C

User Question:
{question}

Instructions:
- Answer in 4–6 sentences.
- Give practical advice.
- Mention clothing, umbrella, travel, health, or outdoor activities whenever relevant.
- Keep the answer concise and friendly.
"""

    last_error = None

    for model in MODELS:

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if response.text:
                return response.text

        except Exception as e:

            last_error = str(e)
            continue

    return (
        "⚠️ Gemini AI is currently unavailable.\n\n"
        "Google's servers may be experiencing high demand. "
        "Please try again in a few minutes.\n\n"
        f"Last Error: {last_error}"
    )