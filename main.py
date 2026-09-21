import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the upcoming days")
place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5, help = "Select the no.of forecast days" )

option = st.selectbox("Select data to view",("Temperature", "Sky"))

if place:
    st.subheader(f"{option} for the next {days} days in {place}")

    filtered_data = get_data(place, days)

    if option == "Temperature":
        temps= [dic["main"]["temp"] for dic in filtered_data]
        dates = [dic["dt_txt"] for dic in filtered_data]
        figure = px.line(x= dates,y= temps,labels ={"x":"Date","y":"Temperature (C)"} )
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                  "Rain":"images/rain.png", "Snow":"images/snow.png"}
        sky_conditions = [dic["weather"][0]["main"] for dic in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width = 115)
