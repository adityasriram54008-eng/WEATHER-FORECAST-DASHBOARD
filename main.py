import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the upcoming days")
place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5, help = "Select the no.of forecast days" )

option = st.selectbox("Select data to view",("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

dates = ["1","2"]
temperatures = ["26","35"]
figure = px.line(x= dates,y= temperatures,labels ={"x":"Date","y":"Temperature (C)"} )
st.plotly_chart(figure)
