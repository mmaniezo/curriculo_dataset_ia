import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.logo("./img/RM.png", size="large")
col1, col2, col3 = st.columns([2, 0.1, 2])  # coluna do meio é mais estreita
with col2:
    st.sidebar.image("./img/logo.png", use_container_width=True)
# Função para carregar o dataset
@st.cache_data
def load_data():
    return pd.read_csv("ai_job_market_insights.csv")

st.markdown(
    "<h1 style='text-align: center;'>Análise de Dados</h1>",
    unsafe_allow_html=True
)
st.title("1. Apresentação dos Dados e Tipos de Variáveis")

# Carregando os dados
try:
    df = load_data()
    st.success("✅ Dataset carregado com sucesso!")

    # Preview do dataset
    st.write("### 🔍 Preview do Dataset")
    st.dataframe(df.head())

    # Informações básicas do dataset
    st.write("### 📊 Sobre oque é o Dataset?")
    st.write("É um Dataset sobre o Poder da IA no Mercado de Trabalho, com foco particular no papel da inteligência artificial (IA) e da automação em vários setores. Esse conjunto de dados inclui 500 empregos únicos, cada uma caracterizada por diferentes fatores, como setor, tamanho da empresa, nível de adoção de IA, risco de automação, habilidades necessárias e projeções de crescimento de empregos. Ele foi projetado para ser um recurso valioso para pesquisadores, cientistas de dados e formuladores de políticas que exploram o impacto da IA no emprego, nas tendências do mercado de trabalho e no futuro do trabalho.")

    # Tipos de variáveis
    st.write("### 🧾 Tipos de Variáveis")
    st.write("""- Job_Title: Qualitativa Nominal.
Representa o título do cargo, como “AI Researcher”, “Cybersecurity Analyst” ou “Marketing Specialist”.
Mesmo sendo texto, não há hierarquia ou ordem lógica entre os cargos.

- Industry: Qualitativa Nominal.
Indica o setor da empresa, como “Technology”, “Entertainment”, “Retail”.
São categorias distintas sem relação de ordem entre si.

- Company_Size: Qualitativa Ordinal.
Classifica o porte da empresa em termos de tamanho, como “Small”, “Medium”, “Large”.
Existe uma ordem natural (pequena < média < grande), o que a torna ordinal.

- Location: Qualitativa Nominal.
Informa o local ou país da vaga, como “Dubai”, “Singapore”, “Berlin”.
Não há hierarquia ou ordenação lógica, ou seja, é apenas uma categorização por local.

- AI_Adoption_Level: Qualitativa Ordinal.
Representa o nível de adoção de Inteligência Artificial na empresa como “Low”, “Medium”, “High”.
Existe uma hierarquia natural (pequena < média < grande), então é ordinal.

- Automation_Risk: Qualitativa Ordinal.
Mostra o risco de automação associado ao cargo, podendo ser “Low”, “Medium” ou “High”.
Essa classificação tem uma escala de intensidade, logo é ordinal.

- Required_Skills: Qualitativa Nominal.
Lista as habilidades exigidas para o cargo, como “UX/UI Design”, “JavaScript”, “Marketing”.
São apenas categorias, sem ordem entre elas.

- Salary_USD: Quantitativa Contínua.
Representa o salário anual em dólares, podendo assumir qualquer valor dentro de um intervalo contínuo, incluindo valores decimais.

- Remote_Friendly: Qualitativa Nominal.
Indica se a vaga é amigável ao trabalho remoto, com valores como “Yes” ou “No”.
Não há hierarquia, apenas categorias distintas.

- Job_Growth_Projection: Qualitativa Nominal.
Representa a projeção de crescimento da vaga no mercado, como “Growth” ou “Decline”.
Não possui escala numérica nem ordem clara, logo é nominal.""")


    # Identificação inicial de perguntas
    st.write("### ❓ Possíveis Perguntas de Análise")
    st.markdown("""
    - Qual é a distribuição dos salários no mercado de IA?  
    - Como os salários variam por nível de adoção de IA e porte da empresa?  
    - Existe alguma dispersão significativa nos salários?  
    - Quais são as categorias mais comuns para cargos, indústrias e níveis de risco de automação? 
    """)

except FileNotFoundError:
    st.error("⚠️ O arquivo 'ai_job_market_insights.csv' não foi encontrado. Verifique se ele está na pasta principal.")




try:
    st.title("2. Medidas Centrais, Distribuição, Dispersão e Correlação")

    st.subheader("- Qual é a distribuição dos salários no mercado de IA?")

    # --- 1. Distribuição dos Salários ---
    fig_dist = px.histogram(
        df, 
        x="Salary_USD", 
        nbins=30, 
        title="Distribuição dos Salários",
        labels={"Salary_USD": "Salário (USD)"},
        color_discrete_sequence=["#636EFA"]
    )
    fig_dist.update_layout(bargap=0.1)
    st.plotly_chart(fig_dist, use_container_width=True)

    # --- 2. Medidas Centrais e Dispersão ---
    st.write("### 📌 Medidas Centrais e Dispersão dos Salários (USD)")
    salario_media = df["Salary_USD"].mean()
    salario_mediana = df["Salary_USD"].median()
    salario_moda = df["Salary_USD"].mode()[0]
    salario_dp = df["Salary_USD"].std()
    salario_var = df["Salary_USD"].var()

    st.write(f"- **Média:** ${salario_media:,.2f}")
    st.write(f"- **Mediana:** ${salario_mediana:,.2f}")
    st.write(f"- **Moda:** ${salario_moda:,.2f}")
    st.write(f"- **Desvio Padrão:** ${salario_dp:,.2f}")
    st.write(f"- **Variância:** ${salario_var:,.2f}")

    st.write("""
    **Resposta:**  
    A distribuição é relativamente simétrica com leve concentração entre US 78k e US 104k. 
    A média e mediana próximas indicam baixa assimetria.
    """)


    st.subheader("- Como os salários variam por nível de adoção de IA e porte da empresa?")
    # --- 3. Salários por Nível de Adoção de IA ---
    fig_box_ai = px.box(
        df, 
        x="AI_Adoption_Level", 
        y="Salary_USD", 
        color="AI_Adoption_Level",
        title="Salários por Nível de Adoção de IA",
        labels={"AI_Adoption_Level": "Nível de Adoção de IA", "Salary_USD": "Salário (USD)"},
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    st.plotly_chart(fig_box_ai, use_container_width=True)

    st.write("""
    **Resposta:**  
    Níveis **High** de adoção de IA apresentam maior variação e salários médios mais altos, 
    sugerindo que empresas com maior integração de IA pagam melhor.
    """)

    st.subheader("- Existe alguma dispersão significativa nos salários?")
    # --- 4. Salários por Porte da Empresa ---
    st.write("### 🏢 Salários por Porte da Empresa")
    fig_box_size = px.box(
        df,
        x="Company_Size",
        y="Salary_USD",
        color="Company_Size",
        title="Salários por Porte da Empresa",
        labels={"Company_Size": "Porte da Empresa", "Salary_USD": "Salário (USD)"},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_box_size, use_container_width=True)

    st.write("""
    **Resposta:**  
    Empresas de porte **Large** apresentam maior média salarial e também maior dispersão. 
    **Small** e **Medium** concentram salários em faixas mais baixas.
    """)


    st.subheader("- Quais são as categorias mais comuns para cargos, indústrias e níveis de risco de automação?")
    # --- 5. Contagem de Cargos Mais Comuns ---
    st.write("### 👨‍💻 Cargos Mais Frequentes")
    top_jobs = df["Job_Title"].value_counts().nlargest(10).reset_index()
    top_jobs.columns = ["Cargo", "Quantidade"]
    fig_jobs = px.bar(
        top_jobs, 
        x="Quantidade", 
        y="Cargo", 
        orientation="h",
        title="Top 10 Cargos no Mercado de IA",
        labels={"Quantidade": "Número de Vagas", "Cargo": "Título do Cargo"},
        color="Quantidade",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig_jobs, use_container_width=True)

    st.write("""
    **Resposta:**  
    Os cargos mais comuns são **AI Researcher** e **Cybersecurity Analyst**, 
    refletindo alta demanda nessas áreas no mercado de IA.
    """)

    # --- 6. Correlação (Salário) ---
    st.write("### 🔗 Correlação entre Variáveis Numéricas")
    corr_value = df.select_dtypes(include='number').corr()
    fig_corr = px.imshow(
        corr_value,
        text_auto=True,
        color_continuous_scale="Viridis",
        title="Mapa de Correlação (Pearson)"
    )
    st.plotly_chart(fig_corr, use_container_width=True)

    st.write("""
    **Resposta:**  
    O único dado numérico é o salário, logo a correlação é trivial (1.0). 
    Para aprofundar, seria necessário transformar variáveis categóricas em numéricas 
    e aplicar técnicas como One-Hot Encoding.
    """)

except FileNotFoundError:
    st.error("⚠️ O arquivo 'ai_job_market_insights.csv' não foi encontrado. Verifique se ele está na pasta principal.")
