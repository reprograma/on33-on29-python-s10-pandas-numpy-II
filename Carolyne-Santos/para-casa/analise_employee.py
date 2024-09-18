# - Analise o dataset Employee e extraia as seguintes informações:
# Bibliotecas

import pandas as pd
import matplotlib.pyplot as plt

#Ler arquivo csv
df = pd.read_csv(r"C:\Users\carol\OneDrive\Área de Trabalho\Reprograma\on33-python-s12-pandas-numpy-II\material\Employee.csv")

#Visualizar meu df
print(df.head())
print(df.describe()) ##retornar informacoes descritivas do dataframe
print(df.info())   ##Retorna as informacoes de valores nulos por coluna e o dtype

##  - Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos:


#Consultar nulos
print(df.isnull().sum())

#Consultar duplicadas
print(df.duplicated().sum())

#Excluir duplicadas
print(df.drop_duplicates(inplace=True))

## - Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos:


#Filtro
mais_5_anos = df.where((df['ExperienceInCurrentDomain'] > 5))

#Visualizar a df com a funcao filtro aplicada
print(mais_5_anos.info())

##  - Agrupe os empregados por gênero e idade e crie um gráfico para cada caso:


#Media, Maxima e Minima idade do df
mean_age = df['Age'].mean()
max_age = df['Age'].max()
min_age = df['Age'].min()

print(f'Idade minina: {min_age}')
print(f'Media de Idade: {round(mean_age)}')
print(f'Idade maxima: {max_age}')

# Agrupar por Gênero e Idade
Age_Female = df[df['Gender'] == 'Female']['Age'].value_counts().sort_index()

# Plotar gráfico para cada gênero
Age_Female.plot(kind='bar', title='Distribuição do Número de Mulheres por Idade')

#visualizar grafico
plt.show()

# Salvar o grafico 
plt.savefig('grafico_barras1.png')  ##para salvar automaticamente o grafico

# Agrupar por Gênero e Idade
Age_Male = df[df['Gender'] == 'Male']['Age'].value_counts().sort_index()

# Plotar gráfico para cada gênero
Age_Male.plot(kind='bar', title='Distribuição do Número de Homens por Idade')

# visualizar grafico
plt.show()

# Salvar o grafico 
plt.savefig('grafico_barras2.png')  ##para salvar automaticamente o grafico

##  - Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade:


#Quantidade de cidades
print(df['City'].value_counts())

#Cidade com a maior quantidade de empregados
mais_empregados = df['City'].value_counts().idxmax()
print(f' A Cidade com a maior quantidade de empregados é: {mais_empregados}')

# Média de tempo de serviço por cidade
# Calcular a média do tempo de serviço por cidade
tempo_medio_servico = df.groupby('City')['ExperienceInCurrentDomain'].mean()

# Exibir a média de tempo de serviço para cada cidade
for cidade, media in tempo_medio_servico.items():
    print(f'A média do tempo de serviço em {cidade} é de: {media:.1f} anos')

## - Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe):


# Considerando
# 0 = O empregado ainda trabalha na empresa.
# 1 = O empregado deixou a empresa.

# Total de empregados
total_empregados = df['LeaveOrNot'].count()

# Total de empregados que ainda trabalham na empresa (LeaveOrNot == 0)
empregados_ativos = df[df['LeaveOrNot'] == 0].count()['LeaveOrNot']

# Cálculo da porcentagem de empregados ativos
porcentagem_ativos = (empregados_ativos / total_empregados) * 100

# Exibir os resultados
print(f'Total de empregados na base de dados: {total_empregados}')
print(f'Total de empregados ativos na empresa: {empregados_ativos}')
print(f'A porcentagem de empregados que ainda trabalham na empresa é: {porcentagem_ativos:.2f}%')

##  - Conte quantos empregados existem por `PaymentTier`: 


# Filtrar os dados onde 'LeaveOrNot' == 0
empregados_ativos = df[df['LeaveOrNot'] == 0]

# Contar quantos empregados existem por 'PaymentTier' entre os que ainda trabalham na empresa
total_filtrado = empregados_ativos['PaymentTier'].value_counts()

# Visualizar o resultado da contagem por 'PaymentTier'
print(total_filtrado)

##  - Substitua os valores da coluna `EverBenched` para `True` ou `False`:


# Substituir valores da coluna 'EverBenched' para 'True' ou 'False'
df['EverBenched'] = df['EverBenched'].replace({'Yes': True, 'No': False})

# Verificar a substituição
print(df[['EverBenched']].head())

# Verificar df depois da alteracao
print(df.head())

##  - Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`:

# Gráfico de pizza para a coluna 'EverBenched'
total_ever_benched = df['EverBenched'].value_counts()
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)  # 1 linha, 2 colunas, gráfico 1. Ultilizado para juntar os graficos  em uma unica tela.
plt.pie(total_ever_benched, labels=total_ever_benched.index, autopct='%1.1f%%') #autopct = define como as %% seram exibidas no grafico.
plt.title('Distribuição de Empregados Disponiveis Para Projetos')

# Gráfico de pizza para a coluna 'LeaveOrNot'
total_leave_or_not = df['LeaveOrNot'].value_counts()
plt.subplot(1, 2, 2)  # 1 linha, 2 colunas, gráfico 2. Ultilizado para juntar os graficos em uma unica tela.
labels = ['Sim' if index == 0 else 'Não' for index in total_leave_or_not.index]
plt.pie(total_leave_or_not, labels=labels, autopct='%1.1f%%') #autopct = define como as %% seram exibidas no grafico.
plt.title('Distribuição de Empregados Ativos')

# Ajustar layout e exibir
plt.tight_layout()
plt.show()

# Salvar o grafico 
plt.savefig('grafico_pizza.png')  ##para salvar automaticamente o grafico