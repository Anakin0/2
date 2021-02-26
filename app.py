import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Add Parameters

'''

date_and_time = st.text_input("Date and Time", "2013-07-06 17:18:00 UTC")
pickup_longitude  = st.text_input("Pickup Longitude", "-73.950655") 
pickup_latitude  = st.text_input("Pickup Latitude", "40.783282")
dropoff_longitude  = st.text_input("Dropoff Longitude", "-73.984365")
dropoff_latitude  = st.text_input("Dropoff Latitude", "40.769802")
passenger_count  = st.text_input("Passenger Count", "1")


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url1 = 'http://taxifare.lewagon.ai/'
url2 = 'http://taxifare.lewagon.ai/predict_fare/'

if url2 == 'http://taxifare.lewagon.ai/predict_fare/':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''
2. Let's build a dictionary containing the parameters for our API...
'''
input_data ={"key":"1",
"pickup_datetime": date_and_time,
"pickup_longitude": pickup_longitude,
"pickup_latitude": pickup_latitude,
"dropoff_longitude": dropoff_longitude,
"dropoff_latitude": dropoff_latitude,
"passenger_count": passenger_count
}

input_data

'''
3. Let's call our API using the `requests` package...
'''
request1 = requests.get(url1)
request1

request2 = requests.get(url2,params=input_data)
request2

'''
4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
prediction = request2.json()
prediction
