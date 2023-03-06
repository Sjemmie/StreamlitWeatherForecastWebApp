import streamlit as st

st.title("Weather forecast for the Next Days")

place = st.text_input(label="Place", placeholder="Enter a city...", key="city")
days = st.slider(label="Forecast days", min_value=1, max_value=5,
                 key="days-slider", help="Select the number of forecasted days")
option = st.selectbox(label="Select type of data to view", options=(["Temperature", "Sky"]), key="dataselect")
st.subheader(f"{option} for the next {days} days in {place}")