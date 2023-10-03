# Import Streamlit and Pandas
import streamlit as st
import pandas as pd
import altair as alt

# Dummy Data for different plots
# Replace these with your actual data
data_reason = pd.DataFrame({
    'reason': ['Password Reset', 'Billing', 'Software Bug', 'Account Locked', 'Others'],
    'count': [100, 80, 50, 40, 30]
})

data_demand = pd.DataFrame({
    'demand': ['Immediate Fix', 'Refund', 'Info', 'Manager Call', 'Others'],
    'count': [90, 70, 60, 50, 40]
})

data_action = pd.DataFrame({
    'action': ['Resolved', 'Escalated', 'Pending', 'Referred', 'Others'],
    'count': [85, 65, 55, 45, 35]
})

data_sentiment = pd.DataFrame({
    'sentiment': ['Positive', 'Negative', 'Neutral'],
    'count': [100, 50, 50]
})

data_upsell = pd.DataFrame({
    'upsell_opportunity': ['True', 'False'],
    'count': [30, 170]
})


# Title
st.title("Desk Trends")

# Create two columns for Plot 1 and Plot 2
col1, col2 = st.columns(2)

# Plot 1: Most common reasons for customers to get in touch
with col1:
    st.subheader("Most Common Reasons for Customer Contact")
    st.bar_chart(data_reason.set_index('reason')['count'])

# Plot 2: Most common demands from customers
with col2:
    st.subheader("Most Common Demands from Customers")
    st.bar_chart(data_demand.set_index('demand')['count'])