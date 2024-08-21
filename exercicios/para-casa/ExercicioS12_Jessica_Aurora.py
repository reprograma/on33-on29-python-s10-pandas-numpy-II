#Analise o dataset Employee e extraia as seguintes informações:
import pandas as pd
df = pd.read_csv(r'C:\Users\Jessica\Desktop\Git-con33\on33-python-s10-pandas-numpy-II\material\Employee.csv')
#print(df.info())
#print(df.describe())

#Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos.
#Irei excluir apenas as linhas duplicadas
#print(df.duplicated().sum())# Verifica total de linhas duplicadas
print (df.drop_duplicates(inplace=True))# Deleta dados duplicados mantendo o primereiro e deletando os demais para cada linha / inplace=True ira modificar o dataframe
#print(df.duplicated().sum())# Verifica total de linhas duplicadas

#Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.
empregados_a_mais_de_5_anos = df[(df['JoiningYear']) < 2017] # Como estamos em 2024 qlqr JoiningYerar acima de 20177 atende ao critério
print(empregados_a_mais_de_5_anos)

#Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.
import matplotlib.pyplot as plt
#print(df.columns)
nome_colunas = df.columns
nome_colunas = nome_colunas.drop(labels=['Education', 'JoiningYear', 'City', 'PaymentTier','EverBenched', 'ExperienceInCurrentDomain', 'LeaveOrNot']) # Exclui colunas descritas e cria um novo df com o resultado
print(nome_colunas)

Genero = df[nome_colunas]# Data frame com colunas Genero e Idade
print(Genero)

Mulheres = Genero[Genero['Gender'] == 'Female'] #Separando o genero feminino e  masculino
Homens = Genero[Genero['Gender'] == 'Male']
#print(Mulheres)
#print(Homens)

def categorizar_idade(valor): #Criando categorias
    if 18 <= valor <= 25:
        return '18-25 anos'
    elif 26 <= valor <= 35:
        return '26-35 anos'
    elif 51 <= valor <= 65:
        return '36-45 anos'
    else:
        return 'Mais de 45 anos'

Mulheres['Categoria Idade'] = Mulheres['Age'].apply(categorizar_idade) # Adicionando as colunas de categorias aos respectivos df's
Homens['Categoria Idade'] = Homens['Age'].apply(categorizar_idade)

categoria_counts_mulheres = Mulheres['Categoria Idade'].value_counts() # Contando o n° de pessoas por categoria
categoria_counts_homens = Homens['Categoria Idade'].value_counts()

#print(categoria_counts_mulheres)
#print(categoria_counts_homens)

categoria_counts_mulheres.plot(kind='bar', title='Mulheres x Idade') # Gerando e imprimindo gráficos por genero
categoria_counts_homens.plot(kind="bar", title='Homens x Idade')
plt.show()

#Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade
cidade_com_mais_empregados = df['City'].value_counts().idxmax() # Nome da icidade/indice correspondente ao valor máximo
numero_de_empregados = df['City'].value_counts().max() # Valor máximo de empregados nessa cidade
print(cidade_com_mais_empregados)
print(numero_de_empregados)

df['TempoDeServico'] = 2024 - df['JoiningYear'] # Diferença entre ano atual e ano de entrada na empresa
media_tempo_servico_por_cidade = df.groupby('City')['TempoDeServico'.mean() # Agrupa e calcula a média com base no tempo de serviço
print(media_tempo_servico_por_cidade)

#Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)
porcentagem_empregados_ativos = (df['LeaveOrNot'].value_counts()[0] / len(df)) * 100 # O 0 representa os empregados que ainda estão na empresa, e 1 representa os que saíram.
print(porcentagem_empregados_ativos)

#Conte quantos empregados existem por `PaymentTier`
contagem_empregados_paymentTier = df['PaymentTier'].value_counts() # calculando/contando n° de empregados 
print(contagem_empregados_paymentTier)

#Substitua os valores da coluna `EverBenched` para `True` ou `False`
df['EverBenched'] = df['EverBenched'].replace({'Yes': True, 'No': False}) # Realizando a substituiçao 
#print(df['EverBenched'].head())

#Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`

Ever = df['EverBenched'].value_counts()
Leave = df['LeaveOrNot'].value_counts()

Ever.plot(kind='pie', title='EverBenched') # Gerando e imprimindo gráficos
Leave.plot(kind="pie", title='LeaveOrNot') # calculando valores
plt.show()