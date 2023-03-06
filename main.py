import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the Next Days")

place = st.text_input(label="Place", placeholder="Enter a city...", key="city")
days = st.slider(label="Forecast days", min_value=1, max_value=5,
                 key="days-slider", help="Select the number of forecasted days")
option = st.selectbox(label="Select type of data to view", options=(["Temperature", "Sky"]), key="dataselect")
st.subheader(f"{option} for the next {days} day(s) in {place}")

data = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "temperature (C)"})
st.plotly_chart(figure)
