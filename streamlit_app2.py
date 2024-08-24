import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("solar-measurements_zambia-fig-tree_ifc_qc.csv")
    df.columns = df.columns.str.strip().str.lower()
    df.rename(columns={
        'time': 'timestamp',
        'dhi_pyr': 'dhi',
        'ghi_pyr_1': 'ghi',
        'air_temperature': 'tamb',
        'barometric_pressure': 'bp',
        'wind_speed': 'ws',
        'wind_from_direction': 'wd'
    }, inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2023-12-31"))

# Filter data by date
df_filtered = df[(df['timestamp'] >= pd.to_datetime(start_date)) & (df['timestamp'] <= pd.to_datetime(end_date))]

# Main Dashboard
st.title("Solar Radiation and Weather Dashboard")

# Summary Statistics
st.header("Summary Statistics")
st.write(df_filtered.describe())

# Time Series Plot
st.header("Time Series Analysis")
fig = px.line(df_filtered, x='timestamp', y=['ghi', 'dhi', 'tamb'],
              title="GHI, DHI, and Ambient Temperature Over Time")
st.plotly_chart(fig)

# Correlation Matrix
st.header("Correlation Matrix")
corr = df_filtered[['ghi', 'dhi', 'tamb', 'ws', 'wd']].corr()
fig_corr = px.imshow(corr, text_auto=True, title="Correlation Matrix")
st.plotly_chart(fig_corr)

# Wind Rose Plot
st.header("Wind Rose Plot")
fig_wind = px.scatter_polar(df_filtered, r='ws', theta='wd', color='ws',
                            title="Wind Speed and Direction", color_continuous_scale='Viridis')
st.plotly_chart(fig_wind)

# Sensor Cleaning Impact
st.header("Sensor Cleaning Impact")
cleaning_effect = df_filtered.groupby('gti_clean').mean()[['ghi', 'dhi', 'tamb']].reset_index()
fig_cleaning = px.bar(cleaning_effect, x='gti_clean', y=['ghi', 'dhi', 'tamb'],
                      title="Impact of Cleaning on Sensor Readings", barmode='group')
st.plotly_chart(fig_cleaning)

# Custom Bubble Chart
st.header("Bubble Chart: GHI vs. Temperature vs. Wind Speed")
fig_bubble = px.scatter(df_filtered, x='ghi', y='tamb', size='ws', color='bp', hover_name='timestamp',
                        title="Bubble Chart: GHI vs. Temperature vs. Wind Speed",
                        labels={'ghi': 'GHI (W/m²)', 'tamb': 'Temperature (°C)', 'ws': 'Wind Speed (m/s)'})
st.plotly_chart(fig_bubble)

# Histogram of Variables
st.header("Histograms of Key Variables")
variables = st.multiselect("Select Variables to Plot Histograms", ['ghi', 'dhi', 'tamb', 'ws'], default=['ghi', 'dhi'])
for var in variables:
    st.subheader(f"Histogram of {var.upper()}")
    fig, ax = plt.subplots()
    sns.histplot(df_filtered[var], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

# Z-Score Analysis for Outliers
st.header("Outlier Detection Using Z-Scores")
z_scores = np.abs(stats.zscore(df_filtered[['ghi', 'dhi', 'tamb', 'ws']].dropna()))
outliers = df_filtered[(z_scores > 3).any(axis=1)]
st.write(f"Number of outliers detected: {outliers.shape[0]}")
st.write(outliers)

# Footer
st.write("Developed by Tihetna Mesfin | © 2024")

