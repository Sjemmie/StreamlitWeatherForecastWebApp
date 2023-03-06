import streamlit as st
import plotly.express as px

st.title("Weather forecast for the Next Days")

place = st.text_input(label="Place", placeholder="Enter a city...", key="city")
days = st.slider(label="Forecast days", min_value=1, max_value=5,
                 key="days-slider", help="Select the number of forecasted days")
option = st.selectbox(label="Select type of data to view", options=(["Temperature", "Sky"]), key="dataselect")
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2022-10-10", "2022-10-11", "2022-10-12"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "temperature (C)"})
st.plotly_chart(figure)
