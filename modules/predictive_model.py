import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st

def prepare_data(df: pd.DataFrame):
    """
    Extract Tickets_Sold from 'Attendance' column and calculate average ticket price.
    """
    attendance_col = 'Attendance (tickets sold / available)'

    # Extract Tickets_Sold and Tickets_Available
    if 'Tickets_Sold' not in df.columns:
        df[['Tickets_Sold', 'Tickets_Available']] = df[attendance_col].str.split('/', expand=True)
        df['Tickets_Sold'] = pd.to_numeric(df['Tickets_Sold'].str.strip(), errors='coerce')
        df['Tickets_Available'] = pd.to_numeric(df['Tickets_Available'].str.strip(), errors='coerce')

    # Calculate average ticket price
    if 'Price' not in df.columns:
        df['Price'] = df['Revenue'] / df['Tickets_Sold']

    return df.dropna(subset=['Tickets_Sold', 'Price'])

def train_model(df: pd.DataFrame):
    """
    Train a simple linear regression model to predict ticket demand from price
    """
    df = prepare_data(df)
    
    if df.empty:
        st.warning("Data is empty or missing required columns for training.")
        return None

    X = df[['Price']]
    y = df['Tickets_Sold']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model

def predict_demand(model, df: pd.DataFrame):
    """
    Predict ticket sales using the trained model
    """
    if model is None:
        st.warning("Model could not be trained.")
        return pd.DataFrame({"Error": ["Model could not be trained"]})

    df = prepare_data(df)
    df['Predicted_Tickets'] = model.predict(df[['Price']])
    
    return df[['Price', 'Tickets_Sold', 'Predicted_Tickets']]
