import streamlit as st
import pandas as pd

st.logo("./img/RM.png", size="large")
col1, col2, col3 = st.columns([2, 0.1, 2])  # coluna do meio é mais estreita
with col2:
    st.sidebar.image("./img/logo.png", use_container_width=True)
# Função para carregar o dataset
@st.cache_data
def load_data():
    return pd.read_csv("ai_job_market_insights.csv")

st.title("Análise de Dados")
st.subheader("Exploração Inicial do Dataset")

try:
    df = load_data()
    st.success("Dataset carregado com sucesso!")
    
    # Preview dos dados
    st.write("### Preview do dataset")
    st.dataframe(df.head())

    # Dimensões do dataset
    st.info(f"O dataset contém **{df.shape[0]} linhas** e **{df.shape[1]} colunas**.")

except FileNotFoundError:
    st.error("⚠️ O arquivo 'ai_job_market_insights.csv' não foi encontrado. Verifique se ele está na pasta principal.")
