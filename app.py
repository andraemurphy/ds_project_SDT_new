import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Sprint 4 Project - Vehicle Ads')

# Load Data
df_vhs = pd.read_csv('vehicles_us.csv')

# Dropdown filters
price_range = st.slider('Select Price Range', int(df_vhs['price'].min()), int(df_vhs['price'].max()), (1000, 20000))
odometer_range = st.slider('Select Odometer Range', int(df_vhs['odometer'].min()), int(df_vhs['odometer'].max()), (0, 100000))
condition_filter = st.multiselect('Select Condition', df_vhs['condition'].unique(), default=df_vhs['condition'].unique())

# Apply filters
df_filtered = df_vhs[(df_vhs['price'] >= price_range[0]) & (df_vhs['price'] <= price_range[1]) &
                      (df_vhs['odometer'] >= odometer_range[0]) & (df_vhs['odometer'] <= odometer_range[1]) &
                      (df_vhs['condition'].isin(condition_filter))]

# Histogram with filtered data
price_hist_filtered = px.histogram(df_filtered, x='price', color='condition', title='Distribution of Vehicle Prices per Condition')

# Scatterplot
display_scatter = st.checkbox('Show Scatterplot')
if display_scatter:
    scat_price_odo = px.scatter(df_filtered, x='odometer', y='price', color='condition',
                                title='Scatterplot Distribution of Price vs Mileage by Condition')
    st.plotly_chart(scat_price_odo)

# Display Histogram
st.plotly_chart(price_hist_filtered)
