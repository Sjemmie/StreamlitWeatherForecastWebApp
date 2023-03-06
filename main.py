import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast")
place = st.text_input(label="Place", placeholder="Enter a city...", key="city")
days = st.slider(label="Forecast days", min_value=1, max_value=5,
                 key="days-slider", help="Select the number of forecasted days")
option = st.selectbox(label="Select type of data to view", options=(["Temperature", "Sky"]), key="dataselect")
st.subheader(f"{option} for the next {days} day(s) in {place}")

# Get the temperature/sky data
try:
    if place:
        filter_data = get_data(place, days)

        # Create a temperature plot
        if option == "Temperature":
            temps = [dict["main"]["temp"] / 10 for dict in filter_data]
            dates = [dict["dt_txt"] for dict in filter_data]
            figure = px.line(x=dates, y=temps, labels={"x": "Date", "y": "temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filter_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
except KeyError:
    st.error("Please enter a valid city")
