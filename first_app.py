import streamlit as st 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
# 

st.title('Uber NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text('Loading Data...')
data = load_data(1000)
data_load_state.text('Loading Completed (using cache)')

hour_to_filter = st.sidebar.slider('hour', 0, 23, 10)  # min: 0h, max: 23h, default: 17h


data_filtered = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

if st.sidebar.checkbox('Want to see raw data ?'):
    st.subheader('Raw Data')
    st.write(data_filtered)

st.subheader('Pickups by Hour')

hist = np.histogram(data[DATE_COLUMN].dt.hour,bins = 24,)[0]

st.bar_chart(hist)


# data2 = data[data[DATE_COLUMN].dt.hour == 10]

st.subheader('Mapping of data')
st.map(data_filtered)



