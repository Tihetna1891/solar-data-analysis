import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset and inspect the column names
df = pd.read_csv('C:/Users/dell/Downloads/new_solar.csv')
print(df.columns)

# Parse the 'time' column as a datetime object
df['time'] = pd.to_datetime(df['time'])

# Perform EDA
summary_stats = df.describe()
print(summary_stats)

# Check for missing values
missing_values = df.isnull().sum()
print(missing_values)

# Check for outliers in specific columns
outliers = df[['dhi_pyr', 'ghi_pyr_1', 'ghi_pyr_2', 'gti_clean', 'gti_soil', 'wind_speed']].quantile([0.01, 0.99])
print(outliers)

# Set 'time' as the index
df.set_index('time', inplace=True)

# Plot time series data for selected columns
df[['dhi_pyr', 'ghi_pyr_1', 'ghi_pyr_2', 'air_temperature']].plot(subplots=True, figsize=(12, 8))
plt.show()

# Correlation matrix and heatmap
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

# Polar plot for wind direction and speed
theta = np.deg2rad(df['wind_from_direction'])
r = df['wind_speed']

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.scatter(theta, r)
plt.show()

# Scatter plot for humidity vs temperature
sns.scatterplot(x='barometric_pressure', y='air_temperature', data=df)
plt.show()

# Histograms for selected variables
df[['dhi_pyr', 'ghi_pyr_1', 'ghi_pyr_2', 'wind_speed', 'air_temperature']].hist(bins=30, figsize=(15, 10))
plt.show()

# Z-score analysis to detect outliers
from scipy import stats

z_scores = np.abs(stats.zscore(df[['dhi_pyr', 'ghi_pyr_1', 'ghi_pyr_2', 'wind_speed', 'air_temperature']]))
outliers_z = df[(z_scores > 3).any(axis=1)]
print(outliers_z)

# Bubble chart using Plotly to explore relationships
import plotly.express as px

fig = px.scatter(df, x='ghi_pyr_1', y='air_temperature', size='barometric_pressure', color='wind_speed', hover_name='time')
fig.show()
