import streamlit as st

st.set_page_config(layout="centered")

st.logo("./img/RM.png", size="large")
col1, col2, col3 = st.columns([2, 0.1, 2])  # coluna do meio é mais estreita
with col2:
    st.sidebar.image("./img/logo.png", use_container_width=True)

col1, col2, col3 = st.columns([1, 20, 1])
with col2:
    st.title("Formação Acadêmica e Experiência")
    st.subheader("Graduação: Engenharia de Software - FIAP")
    st.write("""
    - **Certificações:**  
        - User Experience ⮱ (https://shre.ink/UX)  
        - Leadership Communication ⮱ (https://shre.ink/LCommunication)
        - Formação Social e Sustentabilidade ⮱ (https://shre.ink/FSeSustentabilidade)
        - Inovação Disruptiva ⮱ (https://shre.ink/IDisruptiva)
        - Inteligência Artificial e Computacional ⮱ (https://shre.ink/IAeComputacional)
        - Design Thinking - Process ⮱ (https://shre.ink/DTProcess)
        - Blockchain ⮱ (https://shre.ink/BlocKChain)
    - **Projetos:**  
    """)
col1, col2, col3 = st.columns([1, 20, 1])
with col2:
    st.write("""-
    - Fantasy Game HitRace (Fantasy game de Fórmula E; JavaScript, React, Hooks, CSS; permite criar equipes, acompanhar corridas e pontuação em tempo real)
    """)
col1, col2, col3 = st.columns([1.5, 2, 1.5])
with col2:
    st.image("./img/HitRace.png", use_container_width=True)
    

col1, col2, col3 = st.columns([1, 20, 1])
with col2:
    st.write("""-
    - MacroVision (Sistema de visão computacional para análise de peças patológicas; Python + OpenCV + React; captura imagens, dimensiona amostras e gera relatórios rastreáveis)
    """)
col1, col2, col3 = st.columns([1.5, 2, 1.5])
with col2:
    st.image("./img/macrovision.png", use_container_width=True)


col1, col2, col3 = st.columns([1, 20, 1])
with col2:
    st.write("""-
    - SeaConnect (Plataforma de monitoramento e engajamento ambiental costeiro; Hardware: boias oceânicas inteligentes com sensores IoT para medir qualidade da água, poluição e condições climáticas; Software: Microcontroladores + IoT (MQTT/HTTP) para envio de dados; Dashboard/App: React Native + Google Maps API, com ranking, comunidades e reports; Impacto: conexão de comunidades costeiras, dados abertos sobre poluição marinha, apoio à gestão ambiental e engajamento cidadão.)""")
col1, col2, col3 = st.columns([1.5, 2, 1.5])
with col2:
    st.image("./img/SeaConnect.png", use_container_width=True)


col1, col2, col3 = st.columns([1, 20, 1])
with col2:
    st.write("""-
    - VIBRANIUM (Energia limpa por vibração; Hardware: piezoelétricos + circuitos; Software: Arduino/ESP32 + IoT; Dashboard: React/Python; Impacto: energia sustentável)
     """)
col1, col2, col3 = st.columns([1.5, 2, 1.5])
with col2:
    st.image("./img/vibranium.png", use_container_width=True)

col1, col2, col3 = st.columns([1, 20, 1])
with col2:
    st.write("""-
    - EcoAlert (Prevenção e combate a queimadas; AI + APIs INPE/IBAMA/MapBiomas; App: React Native + Google Maps; Cloud: AWS/Azure; Funcionalidades: mapas preditivos, alertas, denúncias, orientações; Impacto: redução de emergências, apoio a comunidades e agentes de campo)
""")
col1, col2, col3 = st.columns([1.5, 2, 1.5])
with col2:
    st.image("./img/EcoAlert.png", use_container_width=True)
    
    
    
