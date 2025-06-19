# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Set up the Streamlit page
st.set_page_config(page_title="Day-Ahead Solar Forecasting Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to Section:", [
    "Overview",
    "Dataset & Trends",
    "Feature Engineering",
    "Model Performance",
    "Explainability",
    "Insights & Interpretation",
    "Credits"
])

# Helper to load images from relative paths
def load_image(path):
    return Image.open(path)

# Section: Overview
if section == "Overview":
    st.title("Day-Ahead Solar Forecasting Dashboard")
    st.markdown("""
    This project forecasts daily solar power generation in Rajasthan, India, using weather data (NASA POWER) and output data (CEA).
    
    **Goals:**
    - Predict next-day solar energy (MWh) using temperature, radiation, humidity, and other weather variables
    - Evaluate and compare machine learning and time series models
    - Interpret results using explainability tools

    **Models used:**
    - Linear Regression, Random Forest, XGBoost, Neural Network
    - Prophet, SARIMA, SARIMAX
    - SHAP for feature importance
    """)

# Section: Dataset & Trends
elif section == "Dataset & Trends":
    st.header("Dataset and Trend Analysis")
    df = pd.read_csv("data/processed/merged_solar_climate_engineered.csv", parse_dates=["date"])
    st.subheader("Sample of Feature-Engineered Data")
    st.dataframe(df.head(20))  # Show more rows

    st.subheader("Correlation Heatmap")
    st.image(load_image("outputs/corr.png"), use_container_width=True)

    st.subheader("Pairplot: Solar vs Climate Variables")
    st.image(load_image("outputs/pairplot.png"), use_container_width=True)

    st.subheader("Solar Generation and Climate Trends Over Time")
    st.image(load_image("outputs/temporal.png"), use_container_width=True)

# Section: Feature Engineering
elif section == "Feature Engineering":
    st.header("Feature Engineering Techniques")
    st.markdown("""
    This project created over 50 features using:

    - Lag variables (e.g., solar_mwh lagged by 1, 7 days)
    - Rolling means (7-day rolling averages)
    - Cyclical encodings (day_of_week, month as sin/cos)
    - Climate interactions (e.g., wind × radiation)
    - Cloudiness index (clear sky – all sky radiation)
    """)

# Section: Model Performance
elif section == "Model Performance":
    st.header("Model Performance Comparison")

    st.markdown("""
    Performance metrics (after feature engineering):

    | Model              | MAE      | RMSE     | R²     |
    |--------------------|----------|----------|--------|
    | Linear Regression  | 10,069   | 14,561   | 0.66   |
    | Random Forest      | 29,389   | 32,505   | -0.69  |
    | XGBoost            | 31,179   | 34,344   | -0.89  |
    | Neural Network     | 120,861  | 125,441  | -24.2  |
    | Prophet            | 12,171   | 16,648   | 0.735  |
    | Auto-SARIMAX       | 24,376   | 30,871   | 0.325  |
    """)

    st.subheader("Prophet Forecast")
    st.image(load_image("outputs/prophet.png"), use_container_width=True)

    st.subheader("Prophet Trend Components")
    st.image(load_image("outputs/prophet_components.png"), use_container_width=True)

# Section: Explainability
elif section == "Explainability":
    st.header("Model Explainability using SHAP")

    st.markdown("""
    SHAP (SHapley Additive exPlanations) shows feature contributions to predictions.

    **Key Insights:**
    - Past solar generation (lags) is highly predictive
    - Cloudiness and radiation dominate climate influence
    - Humidity, temperature, and wind speed also contribute

    Below is the SHAP summary plot:
    """)
    st.image(load_image("outputs/shap.png"), use_container_width=True)

# Section: Insights
elif section == "Insights & Interpretation":
    st.header("Insights and Interpretation")
    st.markdown("""
    - The best-performing model was Prophet (R² ≈ 0.735)
    - Solar generation shows strong seasonality and trends
    - Previous-day output and radiation levels are the most important predictors
    - SHAP and feature importance confirmed dependence on climate
    - Time series methods outperformed complex ML models (esp. with limited data)
    """)

# Section: Credits
elif section == "Credits":
    st.header("Credits and Acknowledgments")
    st.markdown("""
    - Author: [Your Name]
    - Data Sources:
        - NASA POWER (climate and radiation)
        - CEA Daily Reports (solar output)
    - Tools:
        - Python, pandas, matplotlib, scikit-learn, statsmodels, Prophet, SHAP, Streamlit
    """)
