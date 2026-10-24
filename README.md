# 🌦️ AI Weather Forecast Dashboard

An interactive, AI-powered weather dashboard built using Python and Streamlit as part of my Data Science Internship at **Pinnacle Labs**.

This project combines real-time weather data, AI-generated insights, and interactive visualizations to provide a user-friendly weather monitoring experience.

## ✨ Features

- 🌍 **Location-Based Weather:** Get weather information for a selected location.
- 🌤️ **Weather Forecast:** Explore upcoming weather conditions.
- 🤖 **AI-Powered Insights:** Generate weather-related insights using Google Gemini AI.
- 🌫️ **Air Quality Monitoring:** View air quality information.
- 📊 **Interactive Visualizations:** Explore weather trends using Plotly.
- 📍 **Location Detection:** Support for location-based weather information.
- ⭐ **Favorites:** Save favorite locations for convenient access.
- 🕒 **Weather History:** Access previously stored weather information.
- 🎨 **Interactive Interface:** A user-friendly dashboard developed with Streamlit.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Web application interface |
| WeatherAPI | Weather data and forecasts |
| Google Gemini AI | AI-powered weather insights |
| Plotly | Interactive data visualization |
| Pandas | Data handling and analysis |

## 📁 Project Structure

```text
AI-Weather-Forecast-Dashboard/
├── app.py
├── ai.py
├── air_quality.py
├── css.py
├── favorites.py
├── forecast.py
├── history.py
├── location.py
├── styles.py
├── weather.py
├── test.py
├── requirements.txt
├── favorites.json
├── favourites.json
├── history.json
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ishani19-hub/AI-Weather-Forecast-Dashboard.git
cd AI-Weather-Forecast-Dashboard
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project directory and add the API credentials required by your application.

```env
WEATHER_API_KEY=your_weatherapi_key
GEMINI_API_KEY=your_gemini_api_key
```

Replace these placeholders with your own API keys. Use the exact variable names expected by your Python code. **Never upload your actual API keys to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the dashboard.

## 🎯 Project Objective

The objective of this project is to integrate weather data, generative AI, and data visualization into a single interactive application, making weather information easier to explore and understand.

## 👩‍💻 Developed By

**Ishani Ray Chaudhury**

Developed as part of my Data Science Internship at **Pinnacle Labs**.

---

If you find this project interesting, feel free to explore the repository!
