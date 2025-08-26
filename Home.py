import streamlit as st

# Configuração da página
st.set_page_config(page_title="Dashboard Profissional - Data Science", layout="wide")

# Logo
st.logo("./img/RM.png", size="large")
col1, col2, col3 = st.columns([2, 1, 2])  # coluna do meio é mais estreita
with col2:
    st.image("./img/logo.png", use_container_width=True)

# Conteúdo da Home
st.markdown(
    "<h2 style='text-align: center;'>Olá, eu sou o Rafael Maniezo👋</h2>",
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([1.5, 2, 1.5])  # coluna do meio é mais estreita
with col2:
    st.image("./img/Cruzados.jpg", use_container_width=True)
st.markdown(
    "<h3 style='text-align: center;'>Objetivo Profissional</h3>" \
    "<p style='text-align: center; font-size:18px;'>Sou estudante de Engenharia de Software e este projeto tem um foco em Data Science.<br>Sou apaixonado por análise de dados, machine learning e soluções que unem tecnologia, inovação e diversas outras técnologias!</p>",
    unsafe_allow_html=True
)

