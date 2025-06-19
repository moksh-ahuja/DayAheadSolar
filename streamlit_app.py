# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Day-Ahead Solar Forecasting", layout="wide")

# --- TITLE ---
st.title("🔆 Day-Ahead Solar Generation Forecasting Dashboard")
st.markdown("""
This dashboard showcases an end-to-end pipeline for forecasting day-ahead solar generation in India using weather and energy data.
""")

# --- SIDEBAR ---
st.sidebar.header("📂 Navigation")
section = st.sidebar.radio("Go to:", [
    "Overview",
    "Dataset & Trends",
    "Feature Engineering",
    "Model Comparisons",
    "Model Explainability",
    "Final Insights",
    "Credits"])

# --- HELPER FUNCTION ---
def load_image(path):
    return Image.open(path)

# --- 1. OVERVIEW ---
if section == "Overview":
    st.header("📌 Project Overview")
    st.markdown("""
- 🎯 **Goal**: Forecast next-day solar energy (MWh) using weather and generation data.
- 📊 **Data Sources**: NASA POWER (climate), CEA (solar output)
- 🧠 **ML Models**: Linear Regression, Random Forest, XGBoost, Neural Network
- 🔁 **Time Series**: Prophet, SARIMA, SARIMAX
- 🔬 **Explainability**: SHAP analysis
- ✅ **Best Model**: Prophet (R² ≈ 0.73)
""")

# --- 2. DATASET & TRENDS ---
elif section == "Dataset & Trends":
    st.header("📊 Dataset & Trends")
    df = pd.read_csv("/content/drive/MyDrive/DayAheadSolar/data/processed/merged_solar_climate_engineered.csv", parse_dates=["date"])
    st.subheader("Sample of Feature-Engineered Data")
    st.dataframe(df.head())

    st.subheader("Correlation Heatmap")
    st.image(load_image("/content/drive/MyDrive/DayAheadSolar/outputs/corr.png"), use_column_width=True)

    st.subheader("Pairplot of Climate & Solar Variables")
    st.image(load_image("/content/drive/MyDrive/DayAheadSolar/outputs/pairplot.png"), use_column_width=True)

    st.subheader("Temporal Trends in Solar Output")
    st.image(load_image("/content/drive/MyDrive/DayAheadSolar/outputs/temporal.png"), use_column_width=True)

# --- 3. FEATURE ENGINEERING ---
elif section == "Feature Engineering":
    st.header("🛠️ Feature Engineering Summary")
    st.markdown("""
We created **59+ features** using:
- Lag features (1-day, 7-day)
- Rolling mean features (7-day average)
- Cyclical encodings (month, weekday using sin/cos)
- Novel **cloudiness index** (clear-sky − all-sky radiation)
- Interaction terms: wind × radiation, humidity × temp
- Cumulative and trend-based statistics
""")

# --- 4. MODEL COMPARISONS ---
elif section == "Model Comparisons":
    st.header("🤖 Model Comparisons")

    st.markdown("""
| Model              | MAE     | RMSE     | R²     |
|--------------------|----------|----------|--------|
| Linear Regression  | 10,069   | 14,561   | 0.66   |
| Random Forest      | 29,389   | 32,505   | -0.69  |
| XGBoost            | 31,179   | 34,344   | -0.89  |
| Neural Network     | 120,861  | 125,441  | -24.2  |
| Prophet            | 12,171   | 16,648   | 0.735  |
| Auto-SARIMAX       | 24,376   | 30,871   | 0.325  |
""")

    st.subheader("Prophet Forecast Plot")
    st.image(load_image("/content/drive/MyDrive/DayAheadSolar/outputs/prophet.png"), use_column_width=True)

    st.subheader("Prophet Trend Components")
    st.image(load_image("/content/drive/MyDrive/DayAheadSolar/outputs/prophet_components.png"), use_column_width=True)

# --- 5. MODEL EXPLAINABILITY ---
elif section == "Model Explainability":
    st.header("🔍 SHAP Model Explainability")

    st.markdown("""
SHAP helps us explain feature contributions to predictions.

**Top Drivers**:
- 🔁 Lag features (yesterday’s solar MWh)
- 🌤️ Radiation variables
- 🌫️ Cloudiness index
- 🌬️ Wind speed
- 🌡️ Temperature

**Interpretation**: Red = High feature value, Blue = Low feature value
""")
    st.image(load_image("/content/drive/MyDrive/DayAheadSolar/outputs/shap.png"), use_column_width=True)

# --- 6. FINAL INSIGHTS ---
elif section == "Final Insights":
    st.header("🧾 Final Insights")

    st.markdown("""
- ✅ **Best model**: Prophet (R² ≈ 0.73) — captures both trend and seasonality.
- 🌦️ **Radiation & Cloudiness**: Strongest predictors of generation.
- 🔁 **Lag features**: Yesterday’s output is a solid predictor.
- 📈 **Seasonality**: Prophet captured weekly and annual cycles.
- 🧪 **SARIMAX**: Underperforms unless well-tuned; useful for testing time-lagged variables.
- 📉 **SHAP**: Confirms dependence on physical drivers (radiation, weather) and past output.
""")

# --- 7. CREDITS ---
elif section == "Credits":
    st.header("📜 Credits & Acknowledgments")
    st.markdown("""
- 👨‍💻 **Project by**: [Moksh Ahuja](www.linkedin.com/in/moksh-ahuja)
- 🛰️ **Datasets**:
  - NASA POWER: Climate and radiation variables
  - CEA: Daily solar energy (MWh)
- 🧠 **ML Stack**:
  - Regression, Random Forest, XGBoost, Neural Networks
  - Prophet, SARIMA, SARIMAX (Auto-tuned)
  - SHAP for model explainability
- 🔧 **Tech Used**:
  - pandas, matplotlib, seaborn, sklearn, statsmodels, fbprophet, shap, streamlit
""")
