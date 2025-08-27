import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats

st.set_page_config(layout="centered")

st.logo("./img/RM.png", size="large")
col1, col2, col3 = st.columns([2, 0.1, 2])
with col2:
    st.sidebar.image("./img/logo.png", use_container_width=True)

@st.cache_data
def load_data():
    return pd.read_csv("ai_job_market_insights.csv")

st.sidebar.header("Abas da Análise")
subpagina = st.sidebar.selectbox(
    "Selecione a seção",
    ["Entendendo o Dataset", "Análise do Dataset", "Análise Inferencial"]
)

if subpagina == "Entendendo o Dataset":
    st.markdown(
        "<h1 style='text-align: center;'>Análise de Dados</h1>",
        unsafe_allow_html=True
    )
    st.title("👨‍💻 Apresentação dos Dados e Tipos de Variáveis")

    try:
        df = load_data()
        st.success("✅ Dataset carregado com sucesso!")

        st.write("### 🔍 Preview do Dataset")
        st.dataframe(df.head())

        st.write("### 📊 Sobre oque é o Dataset?")
        st.write("É um Dataset sobre o Poder da IA no Mercado de Trabalho, com foco particular no papel da inteligência artificial (IA) e da automação em vários setores. Esse conjunto de dados inclui 500 empregos únicos, cada uma caracterizada por diferentes fatores, como setor, tamanho da empresa, nível de adoção de IA, risco de automação, habilidades necessárias e projeções de crescimento de empregos. Ele foi projetado para ser um recurso valioso para pesquisadores, cientistas de dados e formuladores de políticas que exploram o impacto da IA no emprego, nas tendências do mercado de trabalho e no futuro do trabalho.")

        st.write("### 🧾 Tipos de Variáveis")
        st.write("""- :
    - Job_Title: Qualitativa Nominal.
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

        st.write("### ❓ Possíveis Perguntas de Análise")
        st.markdown("""
        - Qual é a distribuição dos salários no mercado de IA? 
        - Existe diferença salarial relevante entre níveis de adoção de IA? 
        - O porte da empresa influencia o salário? 
        - Quais cidades oferecem os maiores salários?
        - Existe relação entre adoção de IA, porte da empresa e salários?
        - Quais são as habilidades mais requisitadas no mercado de IA?
        - Qual é a dispersão dos salários por porte da empresa?
        - Como varia a dispersão salarial por nível de adoção de IA?
        """)

    except FileNotFoundError:
        st.error("⚠️ O arquivo 'ai_job_market_insights.csv' não foi encontrado. Verifique se ele está na pasta principal.")

elif subpagina == "Análise do Dataset":
    try:
        df = load_data()
        st.title("📈 Medidas Centrais, Distribuição, Dispersão e Correlação")
        
        st.subheader("- Qual é a distribuição dos salários no mercado de IA?")
        fig_hist = px.histogram(
            df,
            x="Salary_USD",
            nbins=30,
            title="Distribuição dos Salários no Mercado de IA",
            labels={"Salary_USD": "Salário (USD)"},
            color_discrete_sequence=["#636EFA"]
        )
        fig_hist.update_layout(bargap=0.1)
        st.plotly_chart(fig_hist, use_container_width=True)
        st.write("""
        **Resposta:** A maior parte dos salários se concentra entre **78 mil dólares e 104k dólares**, com poucos valores extremos. 
        A média e mediana próximas indicam baixa assimetria. Isso quer dizer que não há concentração exagerada de valores extremos distorcendo a análise. A moda por outro lado não se encaixa muito bem aqui, já que a repetição de valores rara.
        """)

        st.subheader("- Existe diferença salarial relevante entre níveis de adoção de IA?")
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
        **Resposta:** Empresas com **alta adoção de IA** tendem a oferecer **salários mais elevados** e com menor dispersão, 
        enquanto empresas com **nível baixo de adoção** têm uma amplitude maior de salários, indicando mercados menos estáveis.
        """)

        st.subheader("- O porte da empresa influencia o salário?")
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
        **Resposta:** Empresas **Pequenas(Small)** apresentam maior dispersão e **salários ligeiramente mais altos** em média. 
        Já empresas **Grandes(Large)** possuem faixas salariais mais estáveis, refletindo políticas de remuneração padronizadas.
        """)

        st.subheader("- Quais cidades oferecem os maiores salários?")
        salary_by_location = df.groupby("Location")["Salary_USD"].mean().sort_values(ascending=False).reset_index()
        fig_location = px.bar(
            salary_by_location,
            x="Location",
            y="Salary_USD",
            title="Salário Médio por Localização",
            labels={"Location": "Localização", "Salary_USD": "Salário Médio (USD)"},
            color="Salary_USD",
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig_location, use_container_width=True)

        salary_by_location = df.groupby("Location")["Salary_USD"].mean().reset_index()
        city_coords = {
            "San Francisco": {"lat": 37.7749, "lon": -122.4194},
            "New York": {"lat": 40.7128, "lon": -74.0060},
            "Austin": {"lat": 30.2672, "lon": -97.7431},
            "Seattle": {"lat": 47.6062, "lon": -122.3321},
            "Boston": {"lat": 42.3601, "lon": -71.0589},
            "Chicago": {"lat": 41.8781, "lon": -87.6298},
            "Los Angeles": {"lat": 34.0522, "lon": -118.2437},
            "Denver": {"lat": 39.7392, "lon": -104.9903},
            "Atlanta": {"lat": 33.7490, "lon": -84.3880},
            "Miami": {"lat": 25.7617, "lon": -80.1918},
            "Berlin": {"lat": 52.5200, "lon": 13.4050},
            "Dubai": {"lat": 25.276987, "lon": 55.296249},
            "London": {"lat": 51.5074, "lon": -0.1278},
            "Paris": {"lat": 48.8566, "lon": 2.3522},
            "Singapore": {"lat": 1.3521, "lon": 103.8198},
            "Sydney": {"lat": -33.8688, "lon": 151.2093},
            "Tokyo": {"lat": 35.6895, "lon": 139.6917},
            "Toronto": {"lat": 43.65107, "lon": -79.347015},
        }
        salary_by_location["lat"] = salary_by_location["Location"].map(lambda x: city_coords.get(x, {}).get("lat"))
        salary_by_location["lon"] = salary_by_location["Location"].map(lambda x: city_coords.get(x, {}).get("lon"))

        fig_map = px.scatter_mapbox(
            salary_by_location,
            lat="lat",
            lon="lon",
            size="Salary_USD",
            color="Salary_USD",
            hover_name="Location",
            hover_data={"Salary_USD": ":.2f"},
            size_max=40,
            color_continuous_scale="Viridis",
            mapbox_style="carto-positron",
            zoom=1.5,
            title="Mapa dos Salários Médios por Localização"
        )
        st.plotly_chart(fig_map, use_container_width=True)
        st.write("""
        **Resposta:** Com o mapa geográfico e o gráfico de barras, vemos que **Singapore** e **New York** lideram com os **maiores salários médios**, 
        seguindo por polos internacionais como **Berlin**, **Tokyo** e **Paris**. 
        Essas regiões são centros estratégicos para IA, combinando alto custo de vida com alta valorização de talentos.
        """)

        st.subheader("- Existe relação entre adoção de IA, porte da empresa e salários?")
        fig_scatter = px.strip(
            df,
            x="AI_Adoption_Level",
            y="Salary_USD",
            color="Company_Size",
            title="Dispersão de Salários por Nível de Adoção de IA e Porte da Empresa",
            labels={"AI_Adoption_Level": "Nível de Adoção de IA", "Salary_USD": "Salário (USD)", "Company_Size": "Porte da Empresa"},
            color_discrete_sequence=px.colors.qualitative.Set1
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.write("""
        **Resposta:** As empresas **Pequenas(Small)** e **Médias(Medium)** com **alta adoção de IA** tendem a oferecer **salários acima da média**, 
        mostrando que a inovação está associada a uma maior valorização dos profissionais.
        """)

        st.subheader("- Quais são as habilidades mais requisitadas no mercado de IA?")
        skills_series = df["Required_Skills"].value_counts().reset_index()
        skills_series.columns = ["Skill", "Quantidade"]
        fig_skills = px.bar(
            skills_series,
            x="Quantidade",
            y="Skill",
            orientation="h",
            title="Habilidades Mais Demandadas no Mercado de IA",
            labels={"Quantidade": "Quantidade de Vagas", "Skill": "Habilidade"},
            color="Quantidade",
            color_continuous_scale="Blues"
        )
        st.plotly_chart(fig_skills, use_container_width=True)
        st.write("""
        **Resposta:** As habilidades mais requisitadas incluem **Python, Product Manager** e **Cybersecurity**, 
        evidenciando a importância de competências técnicas para profissionais no mercado de IA.
        """)

        st.subheader("- Qual é a dispersão dos salários por porte da empresa?")
        std_by_size = df.groupby("Company_Size")["Salary_USD"].agg(['mean', 'std']).reset_index()
        std_by_size.rename(columns={"mean": "Média", "std": "Desvio Padrão"}, inplace=True)
        fig_std_size = px.bar(
            std_by_size,
            x="Company_Size",
            y="Desvio Padrão",
            color="Desvio Padrão",
            title="Desvio Padrão dos Salários por Porte da Empresa",
            labels={"Company_Size": "Porte da Empresa", "Desvio Padrão": "Desvio Padrão (USD)"},
            color_continuous_scale="Oranges"
        )
        st.plotly_chart(fig_std_size, use_container_width=True)
        st.write("### Tabela Resumida")
        st.dataframe(std_by_size)
        st.write("""
        **Resposta:** O desvio padrão evidencia que **empresas médias apresentam maior dispersão salarial**, 
        indicando grande variação entre cargos e pacotes salariais. 
        Já empresas grandes têm **menor desvio padrão**, mostrando uma política de remuneração mais consistente.
        """)

        st.subheader("- Como varia a dispersão salarial por nível de adoção de IA?")
        var_by_ai = df.groupby("AI_Adoption_Level")["Salary_USD"].agg(['mean', 'var']).reset_index()
        var_by_ai.rename(columns={"mean": "Média", "var": "Variância"}, inplace=True)
        fig_var_ai = px.bar(
            var_by_ai,
            x="AI_Adoption_Level",
            y="Variância",
            color="Variância",
            title="Variância dos Salários por Nível de Adoção de IA",
            labels={"AI_Adoption_Level": "Nível de Adoção de IA", "Variância": "Variância (USD²)"},
            color_continuous_scale="Blues"
        )
        st.plotly_chart(fig_var_ai, use_container_width=True)
        st.write("### Tabela Resumida")
        st.dataframe(var_by_ai)
        st.write("""
        **Resposta:** A variância mostra que empresas com **alto nível de adoção de IA** possuem **maior variabilidade salarial**, 
        enquanto aquelas com **média adoção** apresentam valores mais próximos entre si.
        """)
        st.warning("⚠️O único dado numérico é o salário, logo a correlação é trivial.")

    except FileNotFoundError:
        st.error("⚠️ O arquivo 'ai_job_market_insights.csv' não foi encontrado. Verifique se ele está na pasta principal.")

elif subpagina == "Análise Inferencial":
    try:
        df = load_data()
        st.title("📊 Aplicação de Intervalos de Confiança e Testes de Hipótese")
        st.header("Análise Salarial: Vagas Remotas vs. Presenciais")
        st.write("""
        Nesta seção, vamos investigar se existe uma diferença estatisticamente significativa
        nos salários oferecidos para vagas que são amigáveis ao trabalho remoto ('Remote Friendly')
        em comparação com aquelas que não são.
        """)
        st.subheader("1. Escolha do Parâmetro e Justificativa do Teste")
        st.markdown("""
        - **Parâmetro de Análise:** O Salário em USD.
        - **Grupos de Comparação:** Vagas classificadas como Remote_Friendly **('Yes')** versus as que não são **('No')**.
        - **Ferramentas Estatísticas:**
            - **Teste t de Duas Amostras Independentes:** Foi escolhido por ser a ferramenta ideal para comparar as médias de dois grupos independentes e determinar se a diferença observada é estatisticamente significativa.
            - **Intervalo de Confiança (95%):** Será usado para estimar uma faixa de valores plausíveis para a média salarial real de cada grupo, nos dando mais confiança sobre nossas conclusões.
        """)
        st.subheader("2. Definição das Hipóteses")
        st.markdown(r"""
        Para guiar nossa análise, definimos as seguintes hipóteses:

        - **Hipótese Nula ($H_0$):** Não há diferença entre a média salarial de vagas remotas e não remotas.
          $$
          \mu_{\text{remoto}} = \mu_{\text{não remoto}}
          $$

        - **Hipótese Alternativa ($H_1$):** Existe uma diferença entre a média salarial de vagas remotas e não remotas.
          $$
          \mu_{\text{remoto}} \neq \mu_{\text{não remoto}}
          $$

        Adotaremos um **nível de significância ($\alpha$) de 0.05**. Isso significa que, se o p-valor resultante do teste for menor que 0.05, rejeitaremos a hipótese nula.
        """)
        st.subheader("3. Resultados e Análise Visual")
        salario_remoto_sim = df[df['Remote_Friendly'] == 'Yes']['Salary_USD']
        salario_remoto_nao = df[df['Remote_Friendly'] == 'No']['Salary_USD']
        
        t_stat, p_valor = stats.ttest_ind(salario_remoto_sim, salario_remoto_nao, equal_var=False)
        
        def get_confidence_interval(data, confidence=0.95):
            n = len(data)
            mean = data.mean()
            sem = stats.sem(data)
            interval = sem * stats.t.ppf((1 + confidence) / 2., n - 1)
            return mean, mean - interval, mean + interval
        
        mean_sim, lower_sim, upper_sim = get_confidence_interval(salario_remoto_sim)
        mean_nao, lower_nao, upper_nao = get_confidence_interval(salario_remoto_nao)
        
        st.write("#### Teste de Hipótese:")
        col1, col2 = st.columns(2)
        col1.metric("Estatística t", f"{t_stat:.4f}")
        col2.metric("P-Valor", f"{p_valor:.4f}")
        
        if p_valor < 0.05:
            st.success("""
            **Conclusão do Teste:** Como o p-valor (%.4f) é menor que 0.05, **rejeitamos a Hipótese Nula**.
            Isso significa que existe uma diferença estatisticamente significativa entre os salários de vagas remotas e não remotas.
            """ % p_valor)
        else:
            st.warning("""
            **Conclusão do Teste:** Como o p-valor (%.4f) é maior que 0.05, **não temos evidências para rejeitar a Hipótese Nula**.
            A diferença observada nos salários pode ser meramente casual.
            """ % p_valor)
        
        st.write("#### Intervalos de Confiança (95%) para a Média Salarial:")
        ic_data = {
            "Grupo": ["Remote Friendly (Sim)", "Remote Friendly (Não)"],
            "Média Salarial (USD)": [f"${mean_sim:,.2f}", f"${mean_nao:,.2f}"],
            "IC Inferior (USD)": [f"${lower_sim:,.2f}", f"${lower_nao:,.2f}"],
            "IC Superior (USD)": [f"${upper_sim:,.2f}", f"${upper_nao:,.2f}"]
        }
        st.dataframe(pd.DataFrame(ic_data), use_container_width=True)
        st.write("""
        Os intervalos de confiança mostram a faixa provável para a verdadeira média salarial de cada grupo.
        Como os intervalos não se sobrepõem, isso reforça a conclusão de que as médias salariais dos dois grupos são, de fato, diferentes.
        """)
        
        st.write("#### Visualização Comparativa")
        fig_box = px.box(
            df,
            x="Remote_Friendly",
            y="Salary_USD",
            color="Remote_Friendly",
            title="Comparação Salarial: Vagas Remotas vs. Presenciais",
            labels={"Remote_Friendly": "Amigável ao Trabalho Remoto?", "Salary_USD": "Salário (USD)"},
            color_discrete_map={'Yes': '#00CC96', 'No': '#EF553B'}
        )
        st.plotly_chart(fig_box, use_container_width=True)
        st.markdown("""
        **Conclusão:**

        O teste de hipótese e os intervalos de confiança confirmam o que a visualização quer dizer: **vagas que não são amigáveis ao trabalho remoto **(No)** tendem a ter uma média salarial superior** àquelas que são **(Yes)**.

        Isso pode ser explicado por diversos fatores, como a localização das vagas presenciais em grandes centros urbanos com alto custo de vida (ex: Nova York, Singapura), ou a natureza de cargos mais sênior que exigem presença física. A maior dispersão nos salários de vagas remotas também sugere um mercado mais heterogêneo, com oportunidades que vão desde startups a grandes corporações globais.
        """)

    except FileNotFoundError:
        st.error("⚠️ O arquivo 'ai_job_market_insights.csv' não foi encontrado. Verifique se ele está na pasta principal.")