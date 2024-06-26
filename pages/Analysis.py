import folium.map
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("Analysis of the csv and more")
df = pd.read_csv("datasets/card_transdata.csv")
numOffraud = (df["fraud"] == 1.0).count()
numOflegit = (df["fraud"] == 0.0).count()

data = {'Category':["Fraud","Legit"],"Count":[numOffraud,numOflegit]}
dataoforChart = pd.DataFrame(data)
st.bar_chart(dataoforChart)
st.title("The rise of Credit card fraud")
st.write("Here is map to show place in which fraud has occurred")
map = folium.Map()
dataforMap = pd.read_csv("datasets/data.csv")
latitude = dataforMap["latitude"].to_list()
longitude = dataforMap["longitude"].to_list()
map = folium.Map(location=[0,0],zoom_start=2)
for lat,lon in zip(latitude,longitude):
    folium.Marker([lat,lon],tooltip="Fraud").add_to(map)

st_folium(map)
st.image("images\reginacrimemap.jpg")