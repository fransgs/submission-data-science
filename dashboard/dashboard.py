import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import source as src # data source 

data = src.all_data

#Style
st.markdown("""
        <style>
            .title{
                font-size: 25px !important;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    col1, col2, col3 = st.columns([1,3,1])
    st.subheader('China Meteorological Administration')
    
    with col1:
        st.write("")
        
    with col2:
    #Adding company logo
        st.image("images/CMA.png", width=150)

    with col3:
        st.write("")

st.header(":blue[AIR QUALITY MONITORING]", divider='blue')
#Header
    
col_1, col_2, col_3 = st.columns(3)
with col_1:
    stations = src.get_station(data)
    station = st.selectbox(label="Station", label_visibility='collapsed', options=stations)
    st.write("###")
    
with col_2:
    years = src.get_year(data)
    year = st.selectbox(label="Pollutans", label_visibility='collapsed', options=years)

with col_3:
    months = src.get_month(data, year)
    month = st.selectbox(label="Pollutants", label_visibility='collapsed', options=months)

temp, pres, rh, rain, wind = src.monthly_elements(data, station, year, month)
bar_1, bar_2, bar_3, bar_4, bar_5 = st.columns(5)
with bar_1:
    st.image("images/temperature.png", width=100)
    st.metric("Temperature", value=f"{temp} °C")
with bar_2:
    st.image("images/pressure.png", width=100)
    st.metric("Pressure", value=f"{pres} hPa")
with bar_3:
    st.image("images/humidity.png", width=100)
    st.metric("Relative Humidity", value=f"{rh} %")
with bar_4:
    st.image("images/rain.png", width=100)
    st.metric("Rainfall", value=f"{rain} inc")
with bar_5:
    st.image("images/wind_speed.png", width=100)
    st.metric("Wind Speed", value=f"{wind} MPh")

tab1, tab2 = st.tabs(["📈 Overview", "🗃 Details"])
with tab1:
    column1, column2 = st.columns(2)
    
    # Rata-rata total semua polutan dalam perhari
    with column1:
        with st.container():
            monthly_pollutants = src.monthly_pollutants(data, station, year, month)
            fig = px.line(monthly_pollutants,
                        title="Average Pollutants Daily",
                        labels={"day": "Days", "value": "µg/m³", "variable": "Pollutants"},
                        color_discrete_sequence=["#0068c9", "#83c9ff", "#29b09d", "#7defa1", "#ff2b2b", "#ffabab"])
            fig.update_traces(showlegend=True, mode="lines+markers")
            st.write(fig)
    
    # Rata-rata tiap polutan dalam bulan
    with column2:
        with st.container():
            pollutants = src.pollutan_by_month(data, station, year, month)
            fig = px.bar(pollutants,
                        orientation='h',
                        title="Average Pollutants Monthly",
                        labels={"index": "Pollutants", "value": "µg/m³"},
                        color=pollutants.index,
                        color_discrete_sequence=["#ff2b2b", "#83c9ff", "#0068c9", "#7defa1", "#29b09d", "#ffabab"])
            fig.update_traces(showlegend=False)
            st.write(fig)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        pm25 = src.average_pm25(data, station, year, month)
        fig = px.line(pm25, 
                    title="PM2.5",
                    labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color='#0068c9', showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        pm10 = src.average_pm10(data, station, year, month)
        fig = px.line(pm10,
                     title="PM10",
                     labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color="#83c9ff", showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)
        
    col3, col4 = st.columns(2)
    with col3:
        SO2 = src.average_SO2(data, station, year, month)
        fig = px.line(SO2,
                     title="SO₂",
                     labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color="#29b09d", showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        NO2 = src.average_NO2(data, station, year, month)
        fig = px.line(NO2,
                     title="NO₂",
                     labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color="#7defa1", showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)

    col5, col6 = st.columns(2)
    with col5:
        CO = src.average_CO(data, station, year, month)
        fig = px.line(CO,
                     title="CO",
                     labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color="#ff2b2b", showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)
        
    with col6:
        O3 = src.average_O3(data, station, year, month)
        fig = px.line(O3,
                     title="O₃",
                     labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color="#ffabab", showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)
    
st.caption('Copyright© 2023 China Meteorological Administration All Rights Reserved')
