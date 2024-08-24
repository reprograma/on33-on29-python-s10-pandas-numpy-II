#Importando as bibliotecas 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#Lendo os dados 
df = pd.read_csv('Employee.csv')
##df.head()

#Fazendo a limpeza
df_atualizado = df.drop_duplicates()
df_atualizado

#Valores nullos 
valores_nullos = df_atualizado.isnull().sum()

#Criação do Dataframe
ano_atual = datetime.now().year  
trabalhores_cinco_anos = df_atualizado[(ano_atual - df_atualizado['JoiningYear']) > 5 ]

##Agrupe os empregados por gênero e idade e crie um gráfico para cada caso]
genero_idade_agrupado = trabalhores_cinco_anos.groupby(['Gender', 'Age']).size().reset_index(name='Quantidade')

# Filtrar por gênero masculino
masculino = genero_idade_agrupado[genero_idade_agrupado['Gender'] == 'Male']

# Criar gráfico de barras
plt.bar(masculino['Age'], masculino['Quantidade'], color='pink')
plt.title('Número de Empregados por Idade (Masculino)')
plt.xlabel('Idade')
plt.ylabel('Número de Empregados')
plt.show()

# Filtrar por gênero feminino
mujer = genero_idade_agrupado[genero_idade_agrupado['Gender'] == 'Female']

# Criar gráfico de barras
plt.bar(mujer['Age'], mujer['Quantidade'], color='blue')
plt.title('Número de Empregados por Idade (Masculino)')
plt.xlabel('Idade')
plt.ylabel('Número de Empregados')
plt.show()

##Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade
city_max_employee_value = df['City'].value_counts().idxmax()
print(city_max_employee_value)

##Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe
porcentagem_ainda_trabalhando = df_atualizado['LeaveOrNot'].mean() * 100
contagem_payment_tier = df_atualizado['PaymentTier'].value_counts()
print(porcentagem_ainda_trabalhando)

##Substitua os valores da coluna `EverBenched` para `True` ou `False`
df['EverBenched'] = df['EverBenched'].replace({'No': False, 'Yes': True})
df.head()

##Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`

# Gráfico de Pizza para 'EverBenched'
resultado_everbenched = df['EverBenched'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(resultado_everbenched, labels=resultado_everbenched.index, autopct='%1.1f%%', colors=['Green', 'Black'])
plt.axis('equal')
plt.title('Resultado da Coluna EverBenched')
plt.show()

# Gráfico de Pizza para 'LeaveOrNot'
resultado_leaveornot = df['LeaveOrNot'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(resultado_leaveornot, labels=resultado_leaveornot.index, autopct='%1.1f%%', colors=['Blue', 'Orange'])
plt.axis('equal')
plt.title('Resultado da Coluna LeaveOrNot')
plt.show()