import streamlit as st

st.title("Weather Forecast for the upcoming days")
place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5, help = "Select the no.of forecast days" )

option = st.selectbox("Select data to view",("Temperature", "Sky"))

if place:
    st.subheader(f"{option} for the next {days} days in {place}")