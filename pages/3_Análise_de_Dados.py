import streamlit as st
import pandas as pd

st.logo("RM.png", size="large")
st.sidebar.image("logo.png", width=150)
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
