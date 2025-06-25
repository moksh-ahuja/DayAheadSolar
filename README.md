# DayAheadSolar: Solar Generation Modeling (Rajasthan)

Streamlit: https://dayaheadsolar.streamlit.app/

## Objective  
To model and forecast daily solar energy generation (in MWh) using both statistical time series and machine learning models, with insights from climate and calendar features.

## Data Sources  
- Solar Generation: Daily state-level MU → MWh data (CEA reports)  
- Climate Data: NASA POWER API (temperature, humidity, wind, radiation, etc.)  
- Engineered Features: Lags, rolling means, cyclical calendar encodings, cloudiness index, interactions  

## Models Evaluated  

| Model              | R² Score     | Notes |
|-------------------|--------------|-------|
| Linear Regression | −2.12 → 0.66 | Great improvement post feature engineering |
| Random Forest     | −2.69 → −0.69 | Did not perform well, prone to overfitting |
| XGBoost           | −2.89 → −0.89 | Slightly worse than RF |
| Neural Network    | −28.35 → −24.22 | Not suitable for this scale of data |
| SARIMA            | −0.49         | Poor standalone time series fit |
| SARIMAX (tuned)   | 0.325         | Decent, includes exogenous variables |
| Prophet (best)    | 0.735         | Best-performing model overall 🎯 |

## Key Insights from Modeling

- Top drivers of solar generation (from SHAP):
  - Previous day’s solar generation (lag1)
  - Rolling weekly generation average
  - Solar radiation (all-sky)
  - Cloudiness index (clear-sky − all-sky radiation)
  - Temperature & wind speed

- Cloudiness reduces solar output — visible from high SHAP influence of the `cloudiness_index`  
- Lags are highly predictive → yesterday’s generation is a strong indicator for today  
- Weekly seasonality exists → captured well by Prophet and SARIMA (seasonal order)  
- Feature engineering (lags, rolling means, sin/cos encodings) greatly boosted performance  

## Final Recommendation

- Use Prophet for forecasting future generation  
- Incorporate lags and radiation forecasts as input (can improve even more!)  
- For interpretability, SHAP visualizations provide strong justification for feature usage  

## Files Used  

- `solar_clean.csv`, `climate_nasa_power.csv`  
- `merged_solar_climate_engineered.csv` (final modeling file)  


