# Import Streamlit and Pandas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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

# Plot 1: Most common reasons for customers to get in touch
st.subheader("Most Common Reasons for Customer Contact")
st.bar_chart(data_reason.set_index('reason')['count'])

# Plot 2: Most common demands from customers
st.subheader("Most Common Demands from Customers")
st.bar_chart(data_demand.set_index('demand')['count'])

# Plot 3: Most common actions done by helpdesk
st.subheader("Most Common Actions by Helpdesk")
st.bar_chart(data_action.set_index('action')['count'])

# Plot 4: Pie chart for sentiment
st.subheader("Customer Sentiment")
fig, ax = plt.subplots()
ax.pie(data_sentiment['count'], labels=data_sentiment['sentiment'], autopct='%1.1f%%')
st.pyplot(fig)

# Plot 5: Pie chart for upsell or cross-sell opportunity
st.subheader("Upsell or Cross-sell Opportunities")
fig, ax = plt.subplots()
ax.pie(data_upsell['count'], labels=data_upsell['upsell_opportunity'], autopct='%1.1f%%')
st.pyplot(fig)