import streamlit as st
import pandas as pd
import plotly.express as px
     
st.header('Sprint 4 Project - Vehicle Ads')

df_vhs = pd.read_csv('vehicles_us.csv')
color_list = df_vhs['condition']
price_hist = px.histogram(df_vhs, x='price', color = color_list, title='Distribution of All Vehicle Prices per Condition')


scat_price_odo = px.scatter(df_vhs, x='odometer', y='price', color='condition', title='Scatterplot Distribution of Price vs Mileage by Condition')


if st.checkbox('Show Histogram'):
    st.plotly_chart(price_hist)
   
if st.checkbox('Show Scatterplot'):
    st.plotly_chart(scat_price_odo)
