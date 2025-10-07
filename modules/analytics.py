import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def plot_ticket_trends(df):
    """
    Plot ticket sales trends by Tour or City (since Date column is missing)
    """
    if 'Tickets_Sold' in df.columns:
        # Group by Tour and sum tickets sold
        trend = df.groupby('Tour')['Tickets_Sold'].sum().sort_values(ascending=False)
        
        st.subheader("Ticket Sales by Tour")
        st.bar_chart(trend)
    else:
        st.warning("Column 'Tickets_Sold' not found in data.")
