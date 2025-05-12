
This will predict and forecast the air quality of kathmandu 
# Comprehensive Analysis, prediction and Forecasting of Air Quality in Kathmandu

This project aims to predict and analyze the Air Quality Index (AQI) for Kathmandu, Nepal. The model predicts AQI levels using environmental data and provides insights into the air quality of the city. By forecasting AQI values, the project helps in understanding air pollution trends and its potential health impacts.

🔗 **Live App:** [kathmanduairqualityforecasting.streamlit.app](https://kathmanduairqualityforecasting.streamlit.app)

---

##  📚 Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Features](#features)
- [Methodology](#methodology)
- [Models Used](#models-used)
- [Dashboard Preview](#dashboard-preview)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [Run Locally](#run-locally)
- [Results](#results)
- [References](#references)

---

## 📌 Project Overview
Air pollution in Kathmandu has become a growing public health concern due to the rapid industrialization, vehicular emissions, and construction activities. This project provides a comprehensive analysis and predictive framework for monitoring and forecasting the **Air Quality Index (AQI)** using historical air quality and environmental data.

By utilizing statistical modeling and machine learning, we built:
- A **predictive AQI model** based on environmental inputs such as temperature, humidity, and wind speed.
- A **time-series forecasting model** using Facebook Prophet to predict AQI for the upcoming 24-72 hours.
- An interactive **Streamlit dashboard** that offers real-time AQI predictions and historical insights.

**Key Benefits:**
- **Air Quality Forecasting**: Predict future air quality conditions, assisting individuals and policymakers in making informed decisions to protect health.
- **Real-Time Monitoring**: Track AQI in real time using current weather data, providing live insights.
- **Public Health Advisory**: Health advisories based on real-time and forecasted AQI, helping people plan outdoor activities accordingly.

---

## 🎯 Objectives

- **Historical Data Analysis**: Analyze AQI and weather data from Kathmandu to understand the pollution patterns.
- **Short-Term Forecasting**: Predict AQI trends for the next 24, 48, and 72 hours using time-series forecasting models.
- **Real-Time AQI Prediction**: Implement a machine learning model to predict AQI based on current environmental inputs.
- **Interactive Dashboard**: Develop an easy-to-use web app for users to access AQI insights and forecasts.

---

## ⚙️ Features

- **Visualize**: Interactive charts (line, bar, heatmap, pie) for exploring AQI trends, pollution statistics, and category breakdowns.
- **Predict**: Input current environmental parameters (temperature, humidity, wind speed) to get a predicted AQI value and associated health advisories.
- **Forecast**: Use Facebook Prophet to generate AQI forecasts for 24, 48, and 72 hours, and visualize future pollution patterns.
- **Live Dashboard**: The application is deployed online, providing real-time AQI insights and predictions.

---

## 🧪 Methodology

1. **Data Collection**:  
   We used various open-source data sources to gather historical AQI and meteorological data for Kathmandu:
   - Open-Meteo API for weather data (different gases, temperature, humidity, wind speed).

2. **Data Preprocessing**:  
   - Missing values were handled using imputation techniques.
   - Features like temperature, humidity, wind speed, and AQI readings were normalized and rescaled.
   - Time-series data was converted to proper formats for Prophet model training.

3. **Exploratory Data Analysis (EDA)**:  
   - Trends and seasonal effects of air pollution were visualized.
   - Correlation analysis was conducted to determine the relationship between AQI and meteorological factors.

4. **Modeling**:  
   - **Random Forest Regressor**: Trained on historical weather data to predict AQI values in real-time.
   - **Facebook Prophet**: Used for time-series forecasting, providing AQI predictions for the next 72 hours.

5. **Deployment**:  
   The app is deployed on Render, enabling real-time updates and access to users worldwide.

---

## 🧠 Models Used

| Model                   | Purpose                                  | Metric (R² Score) |
|-------------------------|------------------------------------------|-------------------|
| Random Forest Regressor | Predict AQI based on weather data       | 0.87               |
| Facebook Prophet        | Time-series forecasting of AQI (24–72 hrs) |   Time series   |

---

## 📷 Dashboard Preview

![Dashboard Preview](https://i.imgur.com/ROntVyv.png)

---

## 💻 Technologies Used

- **Python**: The primary programming language used in this project.
- **Streamlit**: For building the interactive dashboard.
- **Facebook Prophet**: Time-series forecasting tool for predicting AQI.
- **Scikit-learn**: For machine learning algorithms like Random Forest.
- **Pandas**: Data processing and manipulation.
- **Numpy**: Numerical computations and data structures.
- **Matplotlib, Seaborn, Plotly**: For data visualization and plotting.
- **GitHub**: Version control and collaboration.

---

## 🗂️ Folder Structure
```bash
├── Dashboard/
│   ├── app.py                       # Main Streamlit app
│   ├── model.pkl                    # Trained Random Forest model
│   ├── requirements.txt             # Python dependencies for the project
│   ├── data/
│   │   ├── Air_Quality_dataset_of_kathmandu.csv  # Final processed Data
│   │   ├── data.csv                # Raw AQI data 1
│   │   ├── data2.csv               # Raw AQI data 2
│   ├── notebooks/
│   │   ├── Air_quality_pred_of_ktm.ipynb  # Main notebook for AQI prediction
│   │   └── clean_dataset.ipynb      # Notebook for cleaning and preprocessing the data
│   ├── models/
│   │   ├── prophet_model.py        # Functions for Prophet time-series forecasting
│   ├── .gitattributes              # Git attributes file for LFS (Large File Storage)
│   ├── .gitignore                  # Git ignore file to exclude unwanted files
│   ├── README.md                   # Project documentation
│   └── screenshots/
│       └── Screenshot 2025-03-11 143402.png  


 ```
## 🚀 Run Locally

### 1. Clone the repository
```bash
 git clone https://github.com/saroj-2004/Comprehensive-Analysis-Prediction-and-Forecasting-of-Air-Quality-in-Kathmandu.git
 cd Comprehensive-Analysis-Prediction-and-Forecasting-of-Air-Quality-in-Kathmandu/Dashboard
 ```

### 2. Create virtual environment & activate
```bash
python -m venv venv
source venv/bin/activate(for mac/linux)  # on Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

---

##  📊 Results

- R² Score: The Random Forest Regressor model achieved an R² score of 0.87, indicating high accuracy in real-time AQI prediction.

- Visualization: The project visualizes seasonal trends, daily pollution cycles, and AQI category breakdowns. This helps users understand air quality patterns in Kathmandu.

- Forecasting: The Facebook Prophet model forecasts AQI values for the next 72 hours, enabling accurate air quality predictions.

---

##  📖 References

- [Facebook Prophet Docs](https://facebook.github.io/prophet/docs/quick_start.html)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Open-Meteo API](https://open-meteo.com/en/docs/historical-weather-api)

