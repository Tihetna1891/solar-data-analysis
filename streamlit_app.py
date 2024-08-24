import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from scipy import stats

# Title and Description
st.title("Solar Radiation and Weather Analysis Dashboard")
st.write("This dashboard provides an exploratory data analysis (EDA) of solar radiation and weather parameters.")

# File Uploader
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Parse the 'time' column as datetime
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)

    # Sidebar filters
    st.sidebar.header("Filters")
    start_date = st.sidebar.date_input("Start date", df.index.min().date())
    end_date = st.sidebar.date_input("End date", df.index.max().date())
    
    if start_date > end_date:
        st.sidebar.error("Error: End date must fall after start date.")
    
    # Filter dataframe based on dates
    df_filtered = df.loc[start_date:end_date]

    # Summary Statistics
    st.header("Summary Statistics")
    st.write(df_filtered.describe())

    # Missing Values
    st.header("Missing Values")
    st.write(df_filtered.isnull().sum())

    # Time Series Plots
    st.header("Time Series Analysis")
    st.write("Visualizing GHI, DNI, DHI, and Temperature over time.")
    fig, ax = plt.subplots(4, 1, figsize=(12, 12))
    df_filtered['dhi_pyr'].plot(ax=ax[0], title='DHI over Time')
    df_filtered['ghi_pyr_1'].plot(ax=ax[1], title='GHI Pyr 1 over Time')
    df_filtered['ghi_pyr_2'].plot(ax=ax[2], title='GHI Pyr 2 over Time')
    df_filtered['air_temperature'].plot(ax=ax[3], title='Air Temperature over Time')
    st.pyplot(fig)

    # Correlation Matrix
    st.header("Correlation Matrix")
    corr_matrix = df_filtered.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Polar Plot for Wind Analysis
    st.header("Wind Analysis")
    theta = np.deg2rad(df_filtered['wind_from_direction'])
    r = df_filtered['wind_speed']
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.scatter(theta, r)
    ax.set_title("Wind Speed and Direction")
    st.pyplot(fig)

    # Scatter Plot for Temperature vs Humidity
    st.header("Temperature vs. Barometric Pressure")
    fig = px.scatter(df_filtered, x='barometric_pressure', y='air_temperature', size='wind_speed', color='dhi_pyr', hover_name=df_filtered.index)
    st.plotly_chart(fig)

    # Histograms
    st.header("Histograms of Key Variables")
    fig, ax = plt.subplots(2, 3, figsize=(15, 10))
    df_filtered['dhi_pyr'].plot(kind='hist', bins=30, ax=ax[0, 0], title='DHI')
    df_filtered['ghi_pyr_1'].plot(kind='hist', bins=30, ax=ax[0, 1], title='GHI Pyr 1')
    df_filtered['ghi_pyr_2'].plot(kind='hist', bins=30, ax=ax[0, 2], title='GHI Pyr 2')
    df_filtered['wind_speed'].plot(kind='hist', bins=30, ax=ax[1, 0], title='Wind Speed')
    df_filtered['air_temperature'].plot(kind='hist', bins=30, ax=ax[1, 1], title='Air Temperature')
    st.pyplot(fig)

    # Z-Score Outlier Detection
    st.header("Z-Score Outlier Detection")
    z_scores = np.abs(stats.zscore(df_filtered[['dhi_pyr', 'ghi_pyr_1', 'ghi_pyr_2', 'wind_speed', 'air_temperature']]))
    outliers_z = df_filtered[(z_scores > 3).any(axis=1)]
    st.write(outliers_z)

    # Bubble Chart
    st.header("Bubble Chart Analysis")
    fig = px.scatter(df_filtered, x='ghi_pyr_1', y='air_temperature', size='barometric_pressure', color='wind_speed', hover_name=df_filtered.index)
    st.plotly_chart(fig)

else:
    st.write("Please upload a CSV file to begin analysis.")

