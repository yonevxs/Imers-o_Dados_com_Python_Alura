import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.isnull())

traducao_colunas = {
    'work_year': 'ano_trabalho',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'salario_em_usd',
    'employee_residence': 'residencia',
    'remote_ratio' : 'remoto',
    'company_location': 'localizacao_empresa',
    'company_size':'tamanho_empresa'
}

df.rename(columns=traducao_colunas, inplace=True)
print(df.columns)
print("")
renomear_colunas = {
    'ano_trabalho': 'ano',
    'nivel_experiencia': 'senioridade',
    'tipo_emprego': 'contrato',
    'cargo': 'cargo',
    'salario': 'salario',
    'moeda_salario': 'moeda',
    'salario_em_usd': 'salario_em_usd',
    'residencia_empregado': 'residencia',
    'taxa_remoto' : 'remoto',
    'localizacao_empresa': 'localizacao_empresa',
    'tamanho_empresa':'tamanho_empresa'
}

df.rename(columns=renomear_colunas, inplace=True)
print(df.columns)

traducao_senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

df['senioridade'] = df['senioridade'].replace(traducao_senioridade)

print(df['senioridade'].value_counts())
print("")

print(df["contrato"].value_counts())
print("")

tipo_contrato = {
    'FT': 'Tempo Integral',
    'CT': 'Contrato',
    'PT': 'Meio período',
    'FL': 'Freelancer'
}

df['contrato'] = df['contrato'].replace(tipo_contrato)
print(df['contrato'].value_counts())
print("")

traducao_tamanho_empresa = {
    'M': 'Médio',
    'L': 'Grande',
    'S': 'Pequeno'
}

df['tamanho_empresa'] = df['tamanho_empresa'].replace(traducao_tamanho_empresa)

print(df['tamanho_empresa'].value_counts())
print("")

traducao_remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}

df['remoto'] = df['remoto'].replace(traducao_remoto)

print(df.head())

print(df.isnull().sum())

print(df["ano"].unique())

print(df[df.isnull().any(axis=1)])

import numpy as np
df_salarios = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
})

df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
print(df_salarios)
print("")

df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
print(df_salarios)
print("")

df_temperaturas = pd.DataFrame({
    'dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura': [30, np.nan, np.nan, 28, 27]
})

df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()
print(df_temperaturas)
print("")

df_temperaturas['preenchido_bfill'] = df_temperaturas['temperatura'].bfill()
print(df_temperaturas)
print("")

df_cidades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'cidade' : ['São Paulo', np.nan, 'Curitiba', np.nan, 'Belém']
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('Não informado')
print(df_cidades)
print("")

df_limpo = df.dropna()

print(df_limpo.isnull().sum())
print("")

print(df_limpo.head())
print("")

print(df_limpo.info())
print("")

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
print(df_limpo.head())
print("")

print(df_limpo.info())
print("")

# Plotando dados (criando gráficos)
# plot() - inicializa o gráfico
# kind = tipo de gráfico (barra, pizza etc.)
# Podemos adicionar um título ao gráfico após especificar seu tipo
df_limpo['senioridade'].value_counts().plot(kind='bar', title='Tipos de Senioridade')
plt.show()

import seaborn as sns

# Calculando o salário medio para cada senioridade
''' sns.blarpot() - serve para criar gráficos de barras,
visualizando a relação entre uma variável numérica e uma ou mais
variáveis categóricas '''
# Explicar depois - o que é a função e como ela tira a media
sns.barplot(data = df_limpo, x = 'senioridade', y = 'salario_em_usd' )
plt.show()

# Definindo tamanho da imagem do gráfico
# plt.figure()
# figsize=(x,y) - define o tamanho da figura (largura, altura)
plt.figure(figsize=(8,5))
sns.barplot(data = df_limpo, x = 'senioridade', y = 'salario_em_usd' )

# Adicionando título ao gráfico
plt.title("Salário Médio por Senioridade")

# Adicionando nome aos eixos X e Y
# Adicionando rótulo (label) ao eixo X
plt.xlabel("Senioridade")
plt.ylabel("Salário Médio Anual")

# Exibindo o gráfico
# plt.show() apresenta o gráfico sem aquele texto em cima
plt.show()

# Ordenando as barras do gráficos
''' Método groupby() - Realiza agrupamentos e consegue fazer ordenações em seguida
    esses agrupamentos são feitos de acordo com alguma estatística, no nosso caso,
    pelo valor médio'''

# Primeiro passos a coluna que queremos agrupar, e, em colchetes, passamos a coluna que queremos calcular a estatística
# No caso, é a media
# Para fazer a ordenação de valores, utilizamos o método sort_values()
# e para ordenar do maior para o menor valor, passamos o parâmetro ascending=False

print(df_limpo.groupby('senioridade')['salario_em_usd'].mean().sort_values(ascending=False))

# Vamos salvar a linha anterior em uma variável
# index - junta toda informação e salva na variável
# EXPLICAR - uso do index
ordem_decrescente = df_limpo.groupby('senioridade')['salario_em_usd'].mean().sort_values(ascending=False).index
ordem_crescente = df_limpo.groupby('senioridade')['salario_em_usd'].mean().sort_values(ascending=True).index

# Quando chamamos o index, ele pega o nome de cada uma das linhas
# e traz uma lista contendo a ordem feita na linha anterior
print(ordem_decrescente)
print(ordem_crescente)

# Gráfico - ORDEM DECRESCENTE
# Exibindo o gráfico com a ordem descendente - do Maior para o Menor
plt.figure(figsize=(8,5))

# Passando o parâmetro "order = ordem" para ordenar o gráfico a partir da filtragem que realizamos
sns.barplot(data = df_limpo, x = 'senioridade', y = 'salario_em_usd', order = ordem_decrescente)

plt.title("Salário Médio por Senioridade - Ordem Decrescente")

plt.xlabel("Senioridade")
plt.ylabel("Salário Médio Anual - U$D")

plt.show()

# Gráfico - ORDEM CRESCENTE
plt.figure(figsize=(8,5))
sns.barplot(data = df_limpo, x = 'senioridade', y = 'salario_em_usd', order = ordem_crescente)
plt.title("Salário Médio por Senioridade  - Ordem Crescente")

plt.xlabel("Senioridade")
plt.ylabel("Salário Médio Anual - U$D")

plt.show()

# HISTOGRAMA

plt.figure(figsize=(8,4))

# Para histogramas é utilizada a função histplot(coluna_para_analisar)
# bins - Intervalos entre as barras geradas pelo histograma
# kde - Cria uma linha para entender a distribuição do gráfico
sns.histplot(df_limpo['salario_em_usd'], bins = 50, kde=True)

plt.title("Distribuição Salarial Anual")
plt.xlabel("Salário Anual - U$D")
plt.ylabel("Frequência")

plt.show()

# BOXPLOT
plt.figure(figsize=(8,5))
sns.boxplot(x = df_limpo['salario_em_usd'])
plt.title("Boxplot - Distribuição Salarial Anual")
plt.xlabel("Salário Anual - U$D")
plt.show()

# Fazendo gráfico por Senioridade
ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
plt.figure(figsize=(8,5))

sns.boxplot(x = 'senioridade', y = 'salario_em_usd', data = df_limpo, order = ordem_senioridade)
plt.title("Distribuição Salarial por Senioridade")
plt.xlabel("Salário Anual - U$D")
plt.show()

# Colocando cores nos gráficos
ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
plt.figure(figsize=(8,5))

# palette - Insere uma paleta de cores nos nossos gráficos, ou podemos criar a nossa própria
# hue - Define uma cor para cada categoria da variável que especificarmos
sns.boxplot(x = 'senioridade', y = 'salario_em_usd', data = df_limpo, order = ordem_senioridade, palette='Set2', hue='senioridade')
plt.title("Distribuição Salarial por Senioridade")
plt.xlabel("Salário Anual - U$D")
plt.show()

# Criando gráficos interativos com Plotly
import plotly.express as px

# Criando um gráfico de barras interativo com Plotly
# px.bar() - cria um gráfico de barras
# data_frame - o DataFrame a ser usado
# x - a coluna para o eixo x
# y - a coluna para o eixo y
# title - o título do gráfico
# reset_index - pega somente o nome da coluna, resetando o index - EXPLICAR
fig = px.bar(df_limpo.groupby('senioridade')['salario_em_usd'].mean().sort_values(ascending=False).reset_index(),
             x='senioridade',
             y='salario_em_usd',
             title='Média Salarial por Senioridade',
             labels={'senioridade': 'Senioridade', 'salario_em_usd': 'Salário Médio Anual - U$D'}) # Ordenando as barras
# labels - coloca os rotulos de x e y em uma linha só
# Exibindo o gráfico
fig.show()

# Criando variável para contar a frequência de trabalho remoto
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()

# Definindo quais colunas estamos calculando
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

# Criando gráfico de pizza
pizza = px.pie(remoto_contagem,
               names = 'tipo_trabalho',
               values = 'quantidade',
               title = 'Proporção dos Tipos de Trabalho')
pizza.show()

remoto_contagem = df_limpo['remoto'].value_counts().reset_index()

remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

pizza = px.pie(remoto_contagem,
               names = 'tipo_trabalho',
               values = 'quantidade',
               title = 'Proporção dos Tipos de Trabalho',
               hole = 0.5)
pizza.show()

remoto_contagem = df_limpo['remoto'].value_counts().reset_index()

remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

pizza = px.pie(remoto_contagem,
               names = 'tipo_trabalho',
               values = 'quantidade',
               title = 'Proporção dos Tipos de Trabalho',
               hole = 0.5)

# Exibindo porcentagem e label de cada parte da rosquinha
pizza.update_traces(textinfo = 'percent+label')
pizza.show()

# Filtrando o DataFrame para incluir apenas os Data Scientists
data_scientist = df_limpo[df_limpo['cargo'] == 'Data Scientist']

# Calculando o salário médio por país para Data Scientists e resetando o índice
salario_medio_por_pais = data_scientist.groupby('localizacao_empresa')['salario_em_usd'].mean().reset_index()


