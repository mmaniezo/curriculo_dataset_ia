import streamlit as st

st.set_page_config(layout="centered")

st.logo("./img/RM.png", size="large")
col1, col2, col3 = st.columns([2, 0.1, 2])  # coluna do meio é mais estreita
with col2:
    st.sidebar.image("./img/logo.png", use_container_width=True)
col1, col2, col3 = st.columns([1, 20, 1])
with col2:
  st.title("Minhas Skills")

  st.subheader("Hard Skills")
  st.write("""
  - Python, Pandas, Numpy, Matplotlib, Plotly  
  - Machine Learning
  - JavaScript, React, HTML e CSS
  - Banco de Dados SQL
  - Metodologia SCRUM e Metodologia Ágil
  - Java
  - Redes (Network)
  - AR/VR Modelagem 3D
  - Arduíno e C++
  - Storytelling
  """)

  st.subheader("Soft Skills")
  st.write("""
  - Comunicação eficaz
  - Trabalho em equipe / Colaboração
  - Resolução de problemas
  - Pensamento crítico
  - Criatividade e inovação
  - Adaptabilidade / Flexibilidade
  - Liderança
  - Capacidade de aprendizagem contínua
  - Proatividade
  - Gestão do tempo
  """)
    