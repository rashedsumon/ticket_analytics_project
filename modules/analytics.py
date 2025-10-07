import streamlit as st
import matplotlib.pyplot as plt

def plot_ticket_trends(df):
    """
    Plot ticket sales trends over time
    """
    if 'Date' in df.columns and 'Tickets_Sold' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        trend = df.groupby('Date')['Tickets_Sold'].sum()
        st.line_chart(trend)
    else:
        st.warning("Columns 'Date' or 'Tickets_Sold' not found in data.")
