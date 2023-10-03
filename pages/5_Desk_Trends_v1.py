# Import Streamlit and Pandas
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Desk Trends",
    page_icon="📈",
)

# Dummy Data for different plots
# Replace these with your actual data
data_reason = pd.DataFrame({
    'reason': ['Quitação do empréstimo', 'Envio de boleto', 'Atualizar informações de contato', 'Alteração da data de vencimento do boleto', 'Cliente não respondeu'],
    'count': [100, 80, 50, 40, 4]
})

data_demand = pd.DataFrame({
    'demand': ['Valor de quitação', 'Gerar boleto de quitação', 'Esclarecer problemas com pagamento', 'Negociar novo acordo', 'Resolver problema com juros e multa'],
    'count': [90, 70, 60, 50, 40]
})

data_action = pd.DataFrame({
    'action': ['Enviou o boleto por e-mail', 'Informou forma de pagamento cadastrada', 'Solicitou print da tela de erro', 'Informou como solicitar um empréstimo', 'Informou processo para alterar os dados cadastrais'],
    'count': [85, 65, 55, 45, 35]
})

data_sentiment = pd.DataFrame({
    'sentimento': ['Positive', 'Negative', 'Neutral'],
    'count': [100, 50, 50]
})

data_upsell = pd.DataFrame({
    'oportunidade': ['True', 'False'],
    'count': [30, 170]
})

# Convert 'count' to percentages for sentiment and upsell opportunity
total_sentiment = data_sentiment['count'].sum()
data_sentiment['percentage'] = (data_sentiment['count'] / total_sentiment) * 100

total_upsell = data_upsell['count'].sum()
data_upsell['percentage'] = (data_upsell['count'] / total_upsell) * 100

# Title
st.title("Desk Trends")

# Calculate top reason data
top_reason_row = data_reason.iloc[0]
top_reason = top_reason_row['reason']
top_reason_count = top_reason_row['count']
total_reason_count = data_reason['count'].sum()
top_reason_percentage = (top_reason_count / total_reason_count) * 100
top_reason_percentage = int(round(top_reason_percentage))

st.header("Motivos de contato")

# Create two columns for Plot 4 and Plot 5
col1, col2 = st.columns(2)

with col1:
    # Display the sentence
    sentence = f"{top_reason_percentage}% são para {top_reason}."
    st.subheader(sentence)

with col2:
    chart1 = alt.Chart(data_reason).mark_bar().encode(
        x=alt.X('count:Q', title=None),
        y=alt.Y('reason:O', sort='-x', title=None)
    ).properties(
            width=300,  # Increase the width
            height=200  # Increase the height
        )
    st.altair_chart(chart1, use_container_width=True)


# Calculate top demand data
top_demand_row = data_demand.iloc[0]
top_demand = top_demand_row['demand']
top_demand_count = top_demand_row['count']
total_demand_count = data_demand['count'].sum()
top_demand_percentage = (top_demand_count / total_demand_count) * 100
top_demand_percentage = int(round(top_demand_percentage))

# Create two columns for Plot 4 and Plot 5
col3, col4 = st.columns(2)

with col3:
    st.subheader("Demandas dos clientes")
    chart2 = alt.Chart(data_demand).mark_bar().encode(
        x='count:Q',
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

# Plot 3: Most common actions done by helpdesk
st.subheader("Ações dos atendentes")
chart3 = alt.Chart(data_action).mark_bar().encode(
    x='count:Q',
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
