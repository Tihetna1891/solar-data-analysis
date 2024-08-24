# solar-data-analysis
Overview
This project is focused on analyzing solar radiation and weather parameters using a dataset containing various meteorological readings. The analysis includes Exploratory Data Analysis (EDA) and the development of interactive dashboards using Streamlit.

Project Structure
Branches:

main: Contains the final versions of the EDA and dashboards.
task-1: Used for EDA on Day 1.
dashboard-dev: Dedicated to the ongoing development of the Streamlit dashboards.
Files:

new_solar.csv: The dataset used for analysis and visualization.
eda_analysis.py: Python script for performing EDA.
streamlit_app1.py: Streamlit dashboard focusing on statistical analysis and visualizations.
streamlit_app2.py: Streamlit dashboard with additional features like wind rose plots, data cleaning, and download options.
README.md: Project documentation and usage instructions.
.gitignore: Specifies files and directories to be ignored by Git.
requirements.txt: Contains all the necessary Python packages.
Development Process
Branch Creation:

Created task-1 for initial EDA and data quality checks.
Created dashboard-dev for the development of Streamlit dashboards.
EDA Analysis (task-1):

Loaded the dataset.
Performed summary statistics to understand data distribution.
Checked for missing values and outliers.
Plotted time series for various metrics (GHI, DNI, DHI, etc.).
Visualized correlations between different variables using heatmaps.
Analyzed wind data using polar plots.
Explored the relationship between temperature and humidity.
Streamlit Dashboard 1 (streamlit_app1.py):

Developed an interactive dashboard with features like data filtering, time series plots, heatmaps, and scatter plots.
Implemented polar plots for wind direction and speed.
Streamlit Dashboard 2 (streamlit_app2.py):

Added additional visualizations including pair plots and wind rose plots.
Integrated a data cleaning feature and download option for the cleaned dataset.
Enhanced the user interface with customizable filters.
Merging:

Merged task-1 and dashboard-dev branches into the main branch using Pull Requests (PR).
Usage Instructions
1. Prerequisites
Ensure you have Python installed.
Install the necessary Python packages by running:
bash
Copy code
pip install -r requirements.txt
2. Running the EDA Script
To perform the EDA analysis:

bash
Copy code
python eda_analysis.py
This script will output various statistical measures, plots, and outlier analysis.

3. Running the Streamlit Dashboards
To launch the first Streamlit dashboard:

bash
Copy code
streamlit run streamlit_app1.py
To launch the second Streamlit dashboard:

bash
Copy code
streamlit run streamlit_app2.py
4. Features of Streamlit Dashboards
Dashboard 1 (streamlit_app1.py)
Time Series Analysis: Interactive plots for various metrics over time.
Correlation Heatmap: Visualizes correlations between solar radiation and weather components.
Polar Plots: Analyzes wind direction and speed.
Scatter Plots: Explores relationships between different weather parameters.
Dashboard 2 (streamlit_app2.py)
Enhanced Time Series Analysis: More focused on user-selected features.
Pair Plots: Visualizes relationships between multiple variables.
Wind Rose Plot: A polar plot to visualize wind direction and speed distribution.
Temperature vs Humidity: Detailed analysis of how temperature and humidity correlate.
Data Cleaning: Drops null values and provides a cleaned dataset.
Download Feature: Allows users to download the cleaned dataset as a CSV.
5. Deployment
Both Streamlit dashboards can be deployed to Streamlit Community Cloud by following the deployment steps on their platform.
