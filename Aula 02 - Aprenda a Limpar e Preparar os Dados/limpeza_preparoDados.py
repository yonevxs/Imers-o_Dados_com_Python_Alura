import pandas as pd
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

#Identificando valores nulos
#somando tudo que é nulo
print(df.isnull().sum())

#Trazendo os valores unicos dentro dessa coluna específica
print(df["ano"].unique())

#Exibindo linhas que há ano nulo
print(df[df.isnull().any(axis=1)])

#Criando um novo DataFrame com pandas - tabelas e valores dentrod das tabelas
import numpy as np
df_salarios = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
})

#Tudo que for nulo vai ser preenchido com a média salarial
#fillna = preenche valores nulos. fill de "preencher" e na de "valores nulos"
#Preencher os valores nulos da base de dados df_salario na coluna 'salario
# O df_salario é a base, salario_media é a coluna que será criada na base a partir da media de 'salario', arredondado para duas casas decimais
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
print(df_salarios)
print("")
''' Fazendo o calculo com mediana
    Caso tenha algum valor distoante no DataFrame (um outlier), a media pode ser contaminada com esse valor
    A mediana acaba reduzindo o impacto que um valor fora do padrão pode causar.'''
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
print(df_salarios)
print("")

df_temperaturas = pd.DataFrame({
    'dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura': [30, np.nan, np.nan, 28, 27]
})

# Fazendo o preenchimento de valores nulos
# Criando uma nova coluna de comparação - Antes e Depois de preencher
# Método ffil() - foward fill = completa com o valor anterior
df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()
print(df_temperaturas)
print("")

#bfill() = backward fill - preenchimento posterior
df_temperaturas['preenchido_bfill'] = df_temperaturas['temperatura'].bfill()
print(df_temperaturas)
print("")

df_cidades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'cidade' : ['São Paulo', np.nan, 'Curitiba', np.nan, 'Belém']
})

# fillna() - preenche valores nulos por algum de sua preferência
df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('Não informado')
print(df_cidades)
print("")

'''dropna() - usado para remover linhas ou colunas que contêm
valores ausentes (geralmente representados como NaN)
de um DataFrame ou Series'''
df_limpo = df.dropna()

# Calcula a soma de valores nulos
print(df_limpo.isnull().sum())
print("")

print(df_limpo.head())
print("")

print(df_limpo.info())
print("")

''' assign() - é usado para adicionar novas colunas a um DataFrame
    ou modificar colunas existentes, retornando um novo DataFrame
    com as alterações, sem modificar o original. '''

''' astype() - é usada para alterar o tipo de dados de um objeto,
    como uma coluna em um DataFrame ou um array NumPy'''

# A base de dados vai receber ela mesma reconfigurando (assign)
# toda a coluna "ano", recebendo a coluna "ano" anterior, passando um novo tipo de dado
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
print(df_limpo.head())
print("")

print(df_limpo.info())
print("")
