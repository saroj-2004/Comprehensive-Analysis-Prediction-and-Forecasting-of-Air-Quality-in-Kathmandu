import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
def train_prophet_model(data):
    df =data
    df = df.rename(columns={"Datetime": "ds", "AQI": "y"})  
    
    model = Prophet(interval_width=0.95)  # 95% confidence interval
    model.fit(df)
    
    return model
def forecast_aqi(model, hours=72):
    """Generate AQI forecast for the next 'hours' using the trained model."""
    future_dates = model.make_future_dataframe(periods=hours, freq='H')
    forecast = model.predict(future_dates)



    return forecast


