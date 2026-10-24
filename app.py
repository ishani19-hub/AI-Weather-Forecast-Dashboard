import streamlit as st
import pandas as pd
import plotly.express as px

from weather import get_weather
from forecast import get_forecast
from location import get_location

from history import (
    load_history,
    add_history,
    clear_history
)

from favorites import (
    load_favorites,
    add_favorite,
    remove_favorite
)

from ai import ask_weather_ai
from css import load_css


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="🌦 AI Weather Dashboard",
    page_icon="🌦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# LOAD CSS
# ==========================================

st.markdown(
    load_css(),
    unsafe_allow_html=True
)


# ==========================================
# CACHE
# ==========================================

@st.cache_data(ttl=600)
def cached_weather(city):
    return get_weather(city)


@st.cache_data(ttl=600)
def cached_forecast(city, days):
    return get_forecast(city, days)


# ==========================================
# SESSION STATE
# ==========================================

if "location" not in st.session_state:

    detected = get_location()

    if detected:

        st.session_state.location = detected

    else:

        st.session_state.location = {
            "city": "",
            "country": ""
        }


if "city" not in st.session_state:

    st.session_state.city = (
        st.session_state.location.get(
            "city",
            ""
        )
    )


if "search" not in st.session_state:

    st.session_state.search = False


# ==========================================
# HEADER
# ==========================================

st.markdown(
"""
<div class="title">
🌦 AI Weather Forecast Dashboard
</div>

<div class="subtitle">
Real-Time Weather • Forecast • AQI • Gemini AI
</div>
""",
unsafe_allow_html=True
)


current_location = st.session_state.location

st.info(
    f"📍 Current Location: "
    f"{current_location.get('city','Unknown')}, "
    f"{current_location.get('country','Unknown')}"
)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.header("⚙ Settings")

    city = st.text_input(
        "📍 Enter City",
        value=st.session_state.city
    )

    days = st.slider(
        "Forecast Days",
        1,
        7,
        3
    )

    if st.button("🔍 Get Forecast"):

        st.session_state.city = city

        st.session_state.search = True

        st.rerun()

    st.divider()

    st.subheader("📜 Search History")

    history = load_history()

    if history:

        for i, item in enumerate(history):

            if st.button(
                item,
                key=f"history_{i}"
            ):

                st.session_state.city = item

                st.session_state.search = True

                st.rerun()

    else:

        st.caption("No history available.")

    if st.button("🗑 Clear History"):

        clear_history()

        st.rerun()

    st.divider()

    st.subheader("⭐ Favorite Cities")

    favorites = load_favorites()

    if favorites:

        for i, fav in enumerate(favorites):

            c1, c2 = st.columns([5,1])

            with c1:

                if st.button(
                    fav,
                    key=f"fav_{i}"
                ):

                    st.session_state.city = fav

                    st.session_state.search = True

                    st.rerun()

            with c2:

                if st.button(
                    "❌",
                    key=f"remove_{i}"
                ):

                    remove_favorite(fav)

                    st.rerun()

    else:

        st.caption("No favorite cities.")

    if st.button("➕ Add Current City"):

        if city.strip():

            if add_favorite(city):

                st.success("Added to favorites.")

            else:

                st.warning("City already exists.")
# ==========================================
# MAIN DASHBOARD
# ==========================================

if st.session_state.search:

    city = st.session_state.city.strip()

    if city == "":

        st.warning("Please enter a city name.")

        st.stop()

    current = cached_weather(city)

    if current is None:

        st.error("❌ Unable to fetch weather data.")

        st.stop()

    forecast = cached_forecast(city, days)

    if forecast is None:

        st.error("❌ Unable to fetch forecast.")

        st.stop()

    add_history(city)

    today = forecast[0]

    st.success(f"📍 Weather for {city}")

    # ======================================
    # CURRENT WEATHER
    # ======================================

    st.markdown("## 🌍 Current Weather")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🌡 Temperature",
        f"{current.get('temp', 'N/A')} °C"
    )

    c2.metric(
        "🤗 Feels Like",
        f"{current.get('feels', 'N/A')} °C"
    )

    c3.metric(
        "💧 Humidity",
        f"{current.get('humidity', 'N/A')} %"
    )

    c4.metric(
        "🌬 Wind",
        f"{current.get('wind', 'N/A')} km/h"
    )

    st.divider()

    left, right = st.columns([1, 3])

    with left:

        if current.get("icon"):

            st.image(
                current["icon"],
                width=120
            )

    with right:

        st.subheader(
            current.get(
                "condition",
                "Unknown"
            )
        )

        st.markdown(
f"""
### 📍 {current.get('city','N/A')}, {current.get('country','N/A')}

🕒 **Local Time:** {current.get('time','N/A')}

👁 **Visibility:** {current.get('visibility','N/A')} km

☀️ **UV Index:** {current.get('uv','N/A')}
"""
        )

    st.divider()

    # ======================================
    # FORECAST TABLE
    # ======================================

    st.subheader(f"📅 {days}-Day Forecast")

    df = pd.DataFrame(forecast)

    display_columns = []

    for column in [
        "date",
        "condition",
        "max_temp",
        "avg_temp",
        "min_temp",
        "rain_probability"
    ]:

        if column in df.columns:

            display_columns.append(column)

    st.dataframe(
        df[display_columns],
        width="stretch"
    )

    st.divider()

    # ======================================
    # TEMPERATURE GRAPH
    # ======================================

    graph_columns = []

    for column in [
        "max_temp",
        "avg_temp",
        "min_temp"
    ]:

        if column in df.columns:

            graph_columns.append(column)

    if graph_columns:

        fig = px.line(

            df,

            x="date",

            y=graph_columns,

            markers=True,

            title="🌡 Temperature Trend"

        )

        fig.update_layout(
            height=450,
            xaxis_title="Date",
            yaxis_title="Temperature (°C)"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    st.divider()
    # ======================================
    # SUN & MOON
    # ======================================

    st.subheader("🌅 Sun & Moon")

    s1, s2, s3 = st.columns(3)

    s1.metric(
        "🌄 Sunrise",
        today.get(
            "sunrise",
            "N/A"
        )
    )

    s2.metric(
        "🌇 Sunset",
        today.get(
            "sunset",
            "N/A"
        )
    )

    s3.metric(
        "🌙 Moon Phase",
        today.get(
            "moon_phase",
            "N/A"
        )
    )



    st.divider()



    # ======================================
    # AIR QUALITY
    # ======================================

    st.subheader("🌫 Air Quality Index")

    a1, a2, a3, a4, a5 = st.columns(5)

    a1.metric(
        "PM2.5",
        current.get(
            "pm2_5",
            "N/A"
        )
    )

    a2.metric(
        "PM10",
        current.get(
            "pm10",
            "N/A"
        )
    )

    a3.metric(
        "CO",
        current.get(
            "co",
            "N/A"
        )
    )

    a4.metric(
        "NO₂",
        current.get(
            "no2",
            "N/A"
        )
    )

    a5.metric(
        "O₃",
        current.get(
            "o3",
            "N/A"
        )
    )



    st.divider()



    # ======================================
    # AI ASSISTANT
    # ======================================

    st.subheader("🤖 AI Weather Assistant")

    question = st.text_input(
        "Ask anything about today's weather",
        placeholder="Should I carry an umbrella today?"
    )

    if st.button("💬 Ask AI"):

        if question.strip() == "":

            st.warning(
                "Please enter a question."
            )

        else:

            weather_context = {

                "city": city,

                "temperature": current.get(
                    "temp"
                ),

                "condition": current.get(
                    "condition"
                ),

                "humidity": current.get(
                    "humidity"
                ),

                "wind": current.get(
                    "wind"
                ),

                "uv": current.get(
                    "uv"
                ),

                "rain_probability": today.get(
                    "rain_probability",
                    "N/A"
                ),

                "max_temp": today.get(
                    "max_temp",
                    "N/A"
                ),

                "min_temp": today.get(
                    "min_temp",
                    "N/A"
                )

            }

            with st.spinner(
                "Thinking..."
            ):

                answer = ask_weather_ai(
                    question,
                    weather_context
                )

            st.success(
                answer
            )



else:

    st.markdown(
        """
        # 🌤 Welcome to AI Weather Dashboard

        ## Features

        ✅ Automatic Current Location

        ✅ Live Weather

        ✅ 7-Day Forecast

        ✅ Interactive Temperature Graph

        ✅ Air Quality Index

        ✅ Search History

        ✅ Favourite Cities

        ✅ Gemini AI Weather Assistant

        ### To begin:

        Enter a city from the sidebar and click **Get Forecast**.
        """
    )