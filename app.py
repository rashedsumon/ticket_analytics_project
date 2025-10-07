import streamlit as st
import pandas as pd
from modules.data_processing import clean_data
from modules.analytics import plot_ticket_trends
from modules.predictive_model import train_model, predict_demand

st.set_page_config(page_title="Live Event Ticket Analytics", layout="wide")
st.title("🎟️ Live Event Ticket Analytics Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/Taylor_Train.csv", encoding='utf-8')
    return df

data = load_data()
st.subheader("Raw Data Preview")
st.dataframe(data.head())

# Data Cleaning
st.subheader("Cleaned Data")
cleaned_data = clean_data(data)
st.dataframe(cleaned_data.head())

# Analytics
st.subheader("Ticket Trends")
plot_ticket_trends(cleaned_data)

# Predictive Modeling
st.subheader("Predict Ticket Demand")
model = train_model(cleaned_data)
predictions = predict_demand(model, cleaned_data)
st.write(predictions.head())
