import streamlit as st
import requests
import pandas as pd

'''
# Maders-TaxiFare
'''

#Data to be entered by user
date_and_time = st.sidebar.text_input("Date and Time", "2013-07-06 17:18:00 UTC")
pickup_longitude  = st.sidebar.text_input("Pickup Longitude", "-73.950655") 
pickup_latitude  = st.sidebar.text_input("Pickup Latitude", "40.783282")
dropoff_longitude  = st.sidebar.text_input("Dropoff Longitude", "-73.984365")
dropoff_latitude  = st.sidebar.text_input("Dropoff Latitude", "40.769802")
passenger_count  = st.sidebar.text_input("Passenger Count", "1")

#API url
url = 'http://taxifare.lewagon.ai/predict_fare/'


#Input Data for API
input_data ={"key":"1",
"pickup_datetime": date_and_time,
"pickup_longitude": float(pickup_longitude),
"pickup_latitude": float(pickup_latitude),
"dropoff_longitude": float(dropoff_longitude),
"dropoff_latitude": float(dropoff_latitude),
"passenger_count": passenger_count
}

# API request
request = requests.get(url,params=input_data)

# Prediction
prediction = request.json()
value = round(prediction["prediction"],2)
f"Taxi Fare = {value} $"

map_data = pd.DataFrame({
'lat' : [float(pickup_latitude),float(dropoff_latitude)],
'lon' : [float(pickup_longitude),float(dropoff_longitude)]
})  

st.map(map_data)