import numpy as np
import pandas as pd
import os
 
# get current directory
path = 'submission-data-science/all_data.csv'
all_data = pd.read_csv(path)

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
