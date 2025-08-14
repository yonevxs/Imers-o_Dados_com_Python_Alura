import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.head(10))
print("")
# Para visualizar as informações no VSCode é necessário realizar print()
#Entendendo informações gerais sobre o arquivo
print(df.info())
print("")
#Entendendo informações dentro do Data Frame
print(df.describe())
print("")
#Exibindo tamanho da base
print(df.shape)
print("")
#Imprimindo linhas e colunas
linhas, colunas = df.shape[0], df.shape[1]
print("Linhas:", linhas)
print("Colunas:", colunas)
print("")
#Listando nomes das colunas - atributo
print(df.columns)
print("")
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
print("")
print(df["ano"].value_counts())
print("")
print(df["contrato"].value_counts())
print("")
print(df["remoto"].value_counts())
print("")
print(df["tamanho_empresa"].value_counts())
print("")

# Traduzindo as categorias da coluna 'senioridade'
traducao_senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

df['senioridade'] = df['senioridade'].replace(traducao_senioridade)

# Exibindo a frequência das categorias traduzidas
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

# Traduzindo as categorias da coluna 'tamanho_empresa'
traducao_tamanho_empresa = {
    'M': 'Médio',
    'L': 'Grande',
    'S': 'Pequeno'
}

df['tamanho_empresa'] = df['tamanho_empresa'].replace(traducao_tamanho_empresa)

# Exibindo a frequência das categorias traduzidas
print(df['tamanho_empresa'].value_counts())
print("")

# Traduzindo as categorias da coluna 'remoto'
traducao_remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}

df['remoto'] = df['remoto'].replace(traducao_remoto)

# Exibindo a frequência das categorias traduzidas
print(df['remoto'].value_counts())
print("")

print(df.head())
print("")

#Usando describe() para dados categóricos
print(df.describe(include='object'))
print("")

df.describe()