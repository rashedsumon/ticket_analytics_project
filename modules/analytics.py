import streamlit as st
import pandas as pd

def plot_ticket_trends(df: pd.DataFrame):
    """
    Plot ticket sales trends by Tour.
    If 'Tickets_Sold' column is missing, show a warning.
    """
    if 'Tickets_Sold' not in df.columns:
        st.warning("Column 'Tickets_Sold' not found in the dataset.")
        return

    if 'Tour' not in df.columns:
        st.warning("Column 'Tour' not found in the dataset.")
        return

    # Aggregate ticket sales by Tour
    ticket_trend = df.groupby('Tour')['Tickets_Sold'].sum().sort_values(ascending=False)

    st.subheader("Ticket Sales by Tour")
    st.bar_chart(ticket_trend)
