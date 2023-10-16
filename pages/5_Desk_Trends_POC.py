# Import Streamlit and Pandas
import streamlit as st
import pandas as pd
import altair as alt
from utils import top_label, total_to_percentage
from data import main_data
from datetime import date
from streamlit_extras.tags import tagger_component
from streamlit_extras.metric_cards import style_metric_cards
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Desk Trends",
    page_icon="📈",
)

# Title
st.title("Desk Trends")

#st.sidebar.markdown('This is some text in the sidebar.')

data_reason, data_demand, data_action, data_sentiment, data_upsell, ticket_info = main_data()

# Add date selector to the sidebar
selected_date = st.sidebar.date_input("Escolha uma data:", min_value=date(2023, 9, 30), max_value=date.today())

# Bot selectbox
bot_selection = st.sidebar.selectbox('Escolha um bot:', ['Bot 1', 'Bot 2'])

# Unique queue options based on the selected bot
unique_queues = data_reason[data_reason['bot_id'] == bot_selection]['queue'].unique().tolist()

# Sidebar radio for queue selection
queue_selection = st.sidebar.radio("Escolha uma fila:", unique_queues)

#st.sidebar.markdown("**Tickets analisados:** 500")

# Filter your data based on this queue_selection as well
filtered_data_reason = data_reason[(data_reason['bot_id'] == bot_selection) & (data_reason['queue'] == queue_selection)]
filtered_data_demand = data_demand[(data_demand['bot_id'] == bot_selection) & (data_demand['queue'] == queue_selection)]
filtered_data_action = data_action[(data_action['bot_id'] == bot_selection) & (data_action['queue'] == queue_selection)]
filtered_data_sentiment = data_sentiment[(data_sentiment['bot_id'] == bot_selection) & (data_sentiment['queue'] == queue_selection)]
filtered_data_upsell = data_upsell[(data_upsell['bot_id'] == bot_selection) & (data_upsell['queue'] == queue_selection)]

# Calculate top reason data
top_reason_percentage, top_reason = top_label(filtered_data_reason, 'reason')

st.divider()
st.header("Motivos de contato")

# Create two columns for Plot 4 and Plot 5
col1, col_space0, col2 = st.columns([0.57, 0.06, 0.47])

with col1:
    chart1 = alt.Chart(filtered_data_reason).mark_bar(color='#2083dd').encode(
        x='total:Q',
        y=alt.Y('reason:O', sort='-x', title=None)
    ).properties(
            width=500,  # Increase the width
            height=200  # Increase the height
        )
    st.altair_chart(chart1, use_container_width=True)

# Use the dummy column to create space
with col_space0:
    st.write("")

with col2:
    # Display the sentence
    tagger_component(
    "",
    ["Principal contato"],
    color_name=["blue"],
)
    
    sentence = f"#### **{top_reason}**"
    st.markdown(sentence)
    sentence = f"### **{top_reason_percentage}%**"
    st.markdown(sentence)


# Calculate top demand data
top_demand_percentage, top_demand = top_label(filtered_data_demand, 'demand')

st.divider()
st.header("Demandas dos clientes")

col3, col_space1, col4 = st.columns([0.47, 0.06, 0.47])

with col3:
    chart2 = alt.Chart(filtered_data_demand).mark_bar(color='#2083dd').encode(
        x='total:Q',
        y=alt.Y('demand:O', sort='-x', title=None)
    ).properties(
            width=300,  # Increase the width
            height=200  # Increase the height
        )
    st.altair_chart(chart2, use_container_width=True)

# Use the dummy column to create space
with col_space1:
    st.write("")

with col4:
    # Display the sentence
    tagger_component(
    "",
    ["Principal demanda"],
    color_name=["blue"],
)
    
    sentence = f"#### **{top_demand}**"
    st.markdown(sentence)
    sentence = f"### **{top_demand_percentage}%**"
    st.markdown(sentence)


# Calculate top action data
top_action_percentage, top_action = top_label(filtered_data_action, 'action')

st.divider()
st.header("Ações dos atendentes")


col5, col_space2, col6 = st.columns([0.47, 0.06, 0.47])
with col5:
    # Plot 3: Most common actions done by helpdesk
    chart3 = alt.Chart(filtered_data_action).mark_bar(color='#2083dd').encode(
        x='total:Q',
        y=alt.Y('action:O', sort='-x', title=None)
    ).properties(
            width=300,  # Increase the width
            height=200  # Increase the height
        )
    st.altair_chart(chart3, use_container_width=True)

# Use the dummy column to create space
with col_space2:
    st.write("")

with col6:
    # Display the sentence
    tagger_component(
    "",
    ["Principal ação"],
    color_name=["blue"],
)
    
    sentence = f"#### **{top_action}**"
    st.markdown(sentence)
    sentence = f"### **{top_action_percentage}%**"
    st.markdown(sentence)

st.divider()
st.subheader("Sentimento dos clientes com o atendimento")

col7, col_space3, col8 = st.columns([0.47, 0.06, 0.47])
# Plot 4: Pie chart for sentiment, displayed as percentages
with col7:
    st.subheader("")
    data_sentiment = total_to_percentage(filtered_data_sentiment, 'total')
    custom_color_scale = alt.Scale(
    domain=['Positivo', 'Negativo', 'Neutro'],
    range=['#0669c5', '#fe2f32', '#0096FA']  # You can replace these with your own color codes
    )
    chart4 = alt.Chart(data_sentiment).mark_arc(innerRadius=50).encode(
        theta=alt.Theta('percentage:Q', stack=True),
        color=alt.Color('sentimento:N', scale=custom_color_scale, legend=None),
        tooltip=[alt.Tooltip('sentimento:N'), alt.Tooltip('percentage:Q', format='.1f')] 
    ).properties(
        width=200,
        height=200
    )
    
    text4 = chart4.mark_text(align='center', baseline='middle', dy=-10).encode(
    text='sentimento:N',
    theta=alt.Theta('percentage:Q', stack=True),
    radius=alt.value(115)
)

    final_chart4 = chart4 + text4

    st.altair_chart(final_chart4, use_container_width=True)

# Use the dummy column to create space
with col_space3:
    st.write("")

with col8:
    # Add a selectbox to filter by sentiment
    sentiment_selection = st.selectbox('Escolha um sentimento para ver os tickets:', ['Todos', 'Positivo', 'Negativo', 'Neutro'])
    # Filter ticket_info based on bot, queue, and sentiment selection
    if sentiment_selection != 'Todos':
        filtered_ticket_info = ticket_info[(ticket_info['bot_id'] == bot_selection) & 
                                        (ticket_info['queue'] == queue_selection) & 
                                        (ticket_info['sentimento'] == sentiment_selection)]
    else:
        filtered_ticket_info = ticket_info[(ticket_info['bot_id'] == bot_selection) & 
                                        (ticket_info['queue'] == queue_selection)]
    # Show only ticket_id and user_id columns from the filtered_ticket_info
    st.write(filtered_ticket_info[['sentimento', 'ticket_id', 'user_id']])

st.divider()
st.subheader("Oportunidades de upsell ou cross-sell nos atendimentos")

# Create two columns for Plot 4 and Plot 5
col9, col_space4, col10 = st.columns([0.47, 0.06, 0.47])

# Plot 5: Pie chart for upsell or cross-sell opportunity, displayed as percentages
with col9:
    st.subheader("")
    data_upsell = total_to_percentage(filtered_data_upsell, 'total')
    chart5 = alt.Chart(data_upsell).mark_arc(innerRadius=50).encode(
        theta=alt.Theta('percentage:Q', stack=True),
        color=alt.Color('oportunidade:N', legend=None),
        tooltip=[alt.Tooltip('oportunidade:N'), alt.Tooltip('percentage:Q', format='.1f')]
    ).properties(
        width=210,
        height=210
    )

    text5 = chart5.mark_text(align='center', baseline='middle', dy=-10).encode(
        text='oportunidade:N',
        theta=alt.Theta('percentage:Q', stack=True),
        radius=alt.value(25)
    )

    final_chart5 = chart5 + text5

    st.altair_chart(final_chart5, use_container_width=True)

# Use the dummy column to create space
with col_space4:
    st.write("")

with col10:
    st.markdown('**Detalhes dos tickets com oportunidade**')
    filtered_ticket_info = ticket_info[(ticket_info['bot_id'] == bot_selection) & 
                                    (ticket_info['queue'] == queue_selection) & 
                                    (ticket_info['oportunidade'] == 'Sim')]
    # Show only ticket_id and user_id columns from the filtered_ticket_info
    st.write(filtered_ticket_info[['oportunidade', 'ticket_id', 'user_id']])