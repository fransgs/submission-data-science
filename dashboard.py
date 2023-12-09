import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# get file from current directory
all_data = pd.read_csv("data/all_data.csv")

# convert month name function
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def number_to_month(month_number):
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month_names[month_number - 1]

def month_to_number(month_name):
    month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month_numbers[month_names.index(month_name)]

# label tahun
def get_year(df):
    years = df['year'].unique()
    return years

# data bulan dari dataframe
def get_month(df, year):
    years_df = df[df['year'] == year]
    months = sorted(years_df['month'].unique())
    months = [number_to_month(month) for month in months]
    return months
    
# data stasiun
def get_station(df):
    station = df['station'].unique()
    return station

# list polusi
def get_pollutan():
    return ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]

# list partikel lainnya
def get_elements():
    return ["TEMP", "PRES", "DEWP", "RH", "RAIN", "WSPM"]

# untuk dashboard
# Menggunakan data bulanan
def monthly_elements(df, station, year, month):
    # convert name to number
    month = month_to_number(month)
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    elements = new_df.agg({
        'TEMP': 'mean',
        'PRES': 'mean',
        'RH': 'mean',
        'RAIN': 'mean',
        'WSPM': 'mean'
    })
    return round(elements.TEMP, 1), round(elements.PRES, 1), round(elements.RH, 1), round(elements.RAIN, 1), round(elements.WSPM, 1)

def monthly_pollutants(df, station, year, month):
    # convert name to number
    month = month_to_number(month)
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    pollutan = new_df.groupby(by='day').agg({
        "PM2.5": "mean",
        "PM10": "mean",
        "SO2": "mean",
        "NO2": "mean",
        "CO": "mean",
        "O3": "mean",
    })
    return round(pollutan, 2)

# rata-rata pm2.5
def average_pm25(df, station, year, month):
    # convert name to number
    month = month_to_number(month)
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    new_df = new_df.rename(columns={"PM2.5": "pm25"})
    pm25 = new_df.groupby(by='day').agg({
        'pm25': 'mean'
    })
    return round(pm25, 2)

# rata-rata pm10
def average_pm10(df, station, year, month):
    month = month_to_number(month)
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    pm10 = new_df.groupby(by='day').agg({
        'PM10': 'mean'
    })
    return round(pm10, 2)

# rata-rata SO2
def average_SO2(df, station, year, month):
    month = month_to_number(month)
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    SO2 = new_df.groupby(by='day').agg({
        'SO2': 'mean'
    })
    return round(SO2, 2)

# rata-rata NO2
def average_NO2(df, station, year, month):
    month = month_to_number(month)
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    NO2 = new_df.groupby(by='day').agg({
        'NO2': 'mean'
    })
    return round(NO2, 2)

# rata-rata CO
def average_CO(df, station, year, month):
    month = month_to_number(month)
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    CO = new_df.groupby(by='day').agg({
        'CO': 'mean'
    })
    return round(CO, 2)

# rata-rata O3
def average_O3(df, station, year, month):
    month = month_to_number(month)
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    O3 = new_df.groupby(by='day').agg({
        'O3': 'mean'
    })
    return round(O3, 2)

# rata-rata pollutan bulanan
def pollutan_by_month(df, station, year, month):
    month = month_to_number(month)
    new_df = df[(df['station'] == station) & (df['year'] == year) & (df['month'] == month)]
    pollutan = new_df.agg({
        "PM2.5": "mean",
        "PM10": "mean",
        "SO2": "mean",
        "NO2": "mean",
        "CO": "mean",
        "O3": "mean"
    }).sort_values(ascending=False)
    
    return round(pollutan, 2)

# rata-rata pollutan tahunan
def pollutan_by_year(df, station, year):
    new_df = df[(df['station'] == station) & (df['year'] == year)]
    pollutan = new_df.agg({
        "PM2.5": "mean",
        "PM10": "mean",
        "SO2": "mean",
        "NO2": "mean",
        "CO": "mean",
        "O3": "mean"
    }).sort_values(ascending=False)
    
    return round(pollutan, 2)

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
    stations = get_station(data)
    station = st.selectbox(label="Station", label_visibility='collapsed', options=stations)
    st.write("###")
    
with col_2:
    years = get_year(data)
    year = st.selectbox(label="Pollutans", label_visibility='collapsed', options=years)

with col_3:
    months = get_month(data, year)
    month = st.selectbox(label="Pollutants", label_visibility='collapsed', options=months)

temp, pres, rh, rain, wind = monthly_elements(data, station, year, month)
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
            monthly_pollutants = monthly_pollutants(data, station, year, month)
            fig = px.line(monthly_pollutants,
                        title="Average Pollutants Daily",
                        labels={"day": "Days", "value": "µg/m³", "variable": "Pollutants"},
                        color_discrete_sequence=["#0068c9", "#83c9ff", "#29b09d", "#7defa1", "#ff2b2b", "#ffabab"])
            fig.update_traces(showlegend=True, mode="lines+markers")
            st.write(fig)
    
    # Rata-rata tiap polutan dalam bulan
    with column2:
        with st.container():
            pollutants = pollutan_by_month(data, station, year, month)
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
        pm25 = average_pm25(data, station, year, month)
        fig = px.line(pm25, 
                    title="PM2.5",
                    labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color='#0068c9', showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        pm10 = average_pm10(data, station, year, month)
        fig = px.line(pm10,
                     title="PM10",
                     labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color="#83c9ff", showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)
        
    col3, col4 = st.columns(2)
    with col3:
        SO2 = average_SO2(data, station, year, month)
        fig = px.line(SO2,
                     title="SO₂",
                     labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color="#29b09d", showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        NO2 = average_NO2(data, station, year, month)
        fig = px.line(NO2,
                     title="NO₂",
                     labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color="#7defa1", showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)

    col5, col6 = st.columns(2)
    with col5:
        CO = average_CO(data, station, year, month)
        fig = px.line(CO,
                     title="CO",
                     labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color="#ff2b2b", showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)
        
    with col6:
        O3 = average_O3(data, station, year, month)
        fig = px.line(O3,
                     title="O₃",
                     labels={"day": "Days", "value": "µg/m³"})
        fig.update_traces(line_color="#ffabab", showlegend=False, mode="lines+markers")
        st.plotly_chart(fig, use_container_width=True)
    
st.caption('Copyright© 2023 China Meteorological Administration All Rights Reserved')
