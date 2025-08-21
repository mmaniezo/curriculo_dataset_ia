import streamlit as st

# Configuração da página
st.set_page_config(page_title="Dashboard Profissional - Data Science", layout="wide")

# Logo
st.logo("RM.png", size="large")
st.image("logo.png", width=200)

# Conteúdo da Home
st.title("Olá, eu sou o Rafa 👋")
st.subheader("Objetivo Profissional")
st.write("""
Sou estudante de Engenharia de Software com foco em Data Science.  
Apaixonado por análise de dados, machine learning e soluções que unem tecnologia e inovação.
""")
