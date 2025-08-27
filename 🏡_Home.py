import streamlit as st

st.set_page_config(layout="centered")

# Configuração da página
st.set_page_config(page_title="Dashboard Profissional - Data Science", layout="wide")
resume_file = "./CURRICULO.pdf"

# Logo
st.logo("./img/RM.png", size="large")
logo_col1, logo_col2, logo_col3 = st.columns([2, 1, 2])
with logo_col2:
    st.image("./img/logo.png", use_container_width=True)

# Conteúdo da Home
st.markdown(
    "<h2 style='text-align: center;'>Olá, eu sou o Rafael Maniezo👋</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='text-align: center;'>Objetivo Profissional</h3>" \
    "<p style='text-align: center; font-size:18px;'>Sou estudante de Engenharia de Software e este projeto tem um foco em Data Science.<br>Sou apaixonado por análise de dados, machine learning e soluções que unem tecnologia, inovação e diversas outras técnologias!</p>",
    unsafe_allow_html=True
)

# Coloca a imagem em uma coluna central para controle do tamanho
img_col1, img_col2, img_col3 = st.columns([1.9, 2, 1.9])
with img_col2:
    st.image("./img/Cruzados.jpg", use_container_width=True)

# Cria um novo conjunto de colunas APENAS para o botão, para centralizá-lo
btn_col1, btn_col2, btn_col3 = st.columns([2.4, 1, 2.4])
with btn_col2:
    try:
        with open(resume_file, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Baixar Currículo",
            data=PDFbyte,
            file_name="CURRICULO.pdf",
            mime="application/pdf",
            use_container_width=True # Faz o botão ocupar toda a coluna do meio
        )
    except FileNotFoundError:
        st.warning("Adicione seu currículo em './CURRICULO.pdf'")