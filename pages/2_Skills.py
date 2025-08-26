import streamlit as st

st.logo("RM.png", size="large")
st.sidebar.image("logo.png", width=150)
st.title("Minhas Skills")

st.subheader("Hard Skills")
st.write("""
- Python, Pandas, Numpy, Matplotlib, Plotly  
- Machine Learning (scikit-learn)  
- JavaScript, React  
- Banco de Dados SQL
""")

st.subheader("Soft Skills")
st.write("""
- Trabalho em equipe  
- Comunicação  
- Pensamento crítico  
- Resolução de problemas
""")
    