# Import Streamlit and Pandas
import streamlit as st
import pandas as pd
import altair as alt
from streamlit.hello.utils import top_label

st.set_page_config(
    page_title="Desk Trends",
    page_icon="📈",
)

# Dummy Data for different plots
# Replace these with your actual data
data_reason = pd.DataFrame({
    'reason': ['Quitação do empréstimo', 'Envio de boleto', 'Atualizar informações de contato', 'Alteração da data de vencimento do boleto', 'Cliente não respondeu'],
    'total': [340, 180, 55, 90, 10]
})

data_demand = pd.DataFrame({
    'demand': ['Valor de quitação', 'Gerar boleto de quitação', 'Esclarecer problemas com pagamento', 'Negociar novo acordo', 'Resolver problema com juros e multa'],
    'total': [390, 270, 160, 50, 40]
})

data_action = pd.DataFrame({
    'action': ['Enviou o boleto por e-mail', 'Informou forma de pagamento cadastrada', 'Solicitou print da tela de erro', 'Informou como solicitar um empréstimo', 'Informou processo para alterar os dados cadastrais'],
    'total': [485, 265, 155, 45, 35]
})

data_sentiment = pd.DataFrame({
    'sentimento': ['Positive', 'Negative', 'Neutral'],
    'total': [454, 271, 120]
})

data_upsell = pd.DataFrame({
    'oportunidade': ['True', 'False'],
    'total': [80, 463]
})

# Convert 'total' to percentages for sentiment and upsell opportunity
total_sentiment = data_sentiment['total'].sum()
data_sentiment['percentage'] = (data_sentiment['total'] / total_sentiment) * 100

total_upsell = data_upsell['total'].sum()
data_upsell['percentage'] = (data_upsell['total'] / total_upsell) * 100

# Title
st.title("Desk Trends")

# Calculate top reason data
top_reason_percentage, top_reason = top_label(data_reason, 'reason')

st.header("Motivos de contato")

# Create two columns for Plot 4 and Plot 5
col1, col2 = st.columns(2)

with col1:
    # Display the sentence
    sentence = f"{top_reason_percentage}% são para {top_reason}."
    st.subheader(sentence)

with col2:
    chart1 = alt.Chart(data_reason).mark_bar().encode(
        x='total:Q',
        y=alt.Y('reason:O', sort='-x', title=None)
    ).properties(
            width=300,  # Increase the width
            height=200  # Increase the height
        )
    st.altair_chart(chart1, use_container_width=True)


# Calculate top demand data
top_demand_percentage, top_demand = top_label(data_demand, 'demand')

st.header("Demandas dos clientes")

# Create two columns for Plot 4 and Plot 5
col3, col4 = st.columns(2)

with col3:
    chart2 = alt.Chart(data_demand).mark_bar().encode(
        x='total:Q',
        y=alt.Y('demand:O', sort='-x', title=None)
    ).properties(
            width=300,  # Increase the width
            height=200  # Increase the height
        )
    st.altair_chart(chart2, use_container_width=True)

with col4:
    # Display the sentence
    sentence = f"{top_demand_percentage}% são para {top_demand}."
    st.subheader(sentence)


# Calculate top action data
top_action_percentage, top_action = top_label(data_action, 'action')

st.header("Ações dos atendentes")

# Create two columns for Plot 4 and Plot 5
col5, col6 = st.columns(2)

with col5:
    # Display the sentence
    sentence = f"{top_action_percentage}% são para {top_action}."
    st.subheader(sentence)

with col6:
    # Plot 3: Most common actions done by helpdesk
    chart3 = alt.Chart(data_action).mark_bar().encode(
        x='total:Q',
        y=alt.Y('action:O', sort='-x', title=None)
    ).properties(
            width=300,  # Increase the width
            height=200  # Increase the height
        )
    st.altair_chart(chart3, use_container_width=True)

# Create two columns for Plot 4 and Plot 5
col7, col8 = st.columns(2)

# Plot 4: Pie chart for sentiment, displayed as percentages
with col7:
    st.subheader("Sentimento dos clientes com o atendimento")
    chart4 = alt.Chart(data_sentiment).mark_arc(innerRadius=50).encode(
        theta=alt.Theta('percentage:Q', stack=True),
        color='sentimento:N',
        tooltip=[alt.Tooltip('sentimento:N'), alt.Tooltip('percentage:Q', format='.1f')]
    ).properties(
        width=200,
        height=200
    )
    st.altair_chart(chart4, use_container_width=True)

with col8:
# Plot 5: Pie chart for upsell or cross-sell opportunity, displayed as percentages
    st.subheader("Oportunidades de upsell ou cross-sell nos atendimentos")
    chart5 = alt.Chart(data_upsell).mark_arc(innerRadius=50).encode(
        theta=alt.Theta('percentage:Q', stack=True),
        color='oportunidade:N',
        tooltip=[alt.Tooltip('oportunidade:N'), alt.Tooltip('percentage:Q', format='.1f')]
    ).properties(
        width=200,
        height=200
    )
    st.altair_chart(chart5, use_container_width=True)
