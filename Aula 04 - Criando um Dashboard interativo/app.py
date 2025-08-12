# Importando bibliotecas
import pandas as pd # Análise de Dados
import plotly.express as px # Criação de gráficos interativos
import streamlit as st # Criação de dashboard
import pycountry # Criação do mapa

# Criando layout da página
# ------ Configurações da Página ------
# Defini o título da página, o ícone e o layout para ocupar a largura inteira

st.set_page_config(
    page_title = 'Dashboard de Salários na Área de Dados', # Similar ao title do HTML
    page_icon = '📊',  # Similar ao favicon do HTML
    layout = 'wide' # Deixa a página larga - Explicar depois
)

# --- Carregamento dos dados ---
# Importando DataFrame para usar no dashboard
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

# Criando barra lateral - Filtros
st.sidebar.header("Filtros | 🛠️")

# Filtro - Ano
anos_disponiveis = sorted(df['ano'].unique()) # Pega os valores únicos do df, na linha ano  

# sidebar tras a opção de escolher os anos, passando como parâmetro os anos disponíveis
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default = anos_disponiveis)

# Filtro - Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())

senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

# Filtro - Contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

# Filtro - Tamanho da Empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

# ------ Filtragem do DataFrame  ------
# o DataFrame principal é filtrado baseado nas seleções feitas no sidebar
# Quando o usuário entrar na página e filtrar informações, o df_filtrado será inicializado

df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# ------ Conteúdo Principal ------
st.title("Dashboard - Salários na Área de Dados | 🎲")

#Texto explicativo - Similar ao <p> em HTML
st.markdown("Explore dados sobre os salários na área de Dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

# ------ Métricas Principais (KPIs) ------ 
st.subheader("Métricas gerais (Salário Anual em U$D)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado['cargo'].mode()[0]
else:
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_mais_comum = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"${total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

# ------ Criação de Gráficos com Plotly ------
#Subtítulo
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        #nlargest(10) - Pega os 10 valores maiores
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()

        grafico_cargos = px.bar(
            top_cargos,
            x = 'usd',
            y = 'cargo',
            # Orientação do Gráfico
            orientation = 'h',
            title = 'Top 10 - Cargos por Salário Médio',
            labels = {'usd': 'Média salarial anual (U$D)', 'cargo': ''}
        )
        #title_x=0.1 - Move o titulo para a direita
        grafico_cargos.update_layout(title_x=0.4, yaxis={'categoryorder':'total ascending'})

        #Exibindo gráfico com Streamlit
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Não há nenhum dado para ser exibido no gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title='Distribuição de salários anuais',
            labels={'usd': 'Faixa Salarial (U$D)', 'count': ' '}
        )
        grafico_hist.update_layout(title_x=0.3)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Não há nenhum dado para ser exibido no gráfico de distribuição salarial.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

        grafico_remoto = px.pie(
            remoto_contagem,
            names = 'tipo_trabalho',
            values = 'quantidade',
            title = 'Proporção dos tipos de trabalho',
            hole = 0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning('Nenhum dado para ser exibido no gráfico de tipos de trabalho.')

with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().round(2).reset_index()
        grafico_paises = px.choropleth(media_ds_pais,
        locations = 'residencia_iso3',
        color = 'usd',
        color_continuous_scale = 'rdylgn',
        title = 'Salário Médio por País - Data Scientist',
        labels = {'usd': 'Salário Médio Anual - U$D', 'residencia_iso3': 'País'})

        grafico_paises.update_layout(title_x = 0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Não há nenhum dado para ser exibido no gráfico de países")

# ------ Tabela de Dados Detalhados ------
st.subheader("Dados Detalhados")

st.dataframe(df_filtrado)
st.markdown("Feito por Lucas Henrique Neves Sousa - Imersão Dados com Python - 2025")

