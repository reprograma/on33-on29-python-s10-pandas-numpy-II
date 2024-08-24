import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv("Employee.csv")

# Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos

df_atualizado = df.drop_duplicates() 

print(df_atualizado)

valores_nulos = df.isnull().sum()

print(valores_nulos)

# Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.

ano_atual = datetime.now().year
mais_de_5_anos = df_atualizado [(ano_atual - df_atualizado ['JoiningYear']) > 5]

# Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.

agrupamento_genero_idade = mais_de_5_anos.groupby(['Gender', 'Age']).size().reset_index(name='Contagem')

print(agrupamento_genero_idade )

masculino = agrupamento_genero_idade[agrupamento_genero_idade['Gender'] == 'Male']
plt.bar(masculino['Age'], masculino['Contagem'], color='blue')
plt.title('Número de Empregados por Idade (Masculino)')
plt.xlabel('Idade')
plt.ylabel('Número de Empregados')
plt.show()

feminino = agrupamento_genero_idade[agrupamento_genero_idade['Gender'] == 'Female']
plt.bar(feminino['Age'], feminino['Contagem'], color='pink')
plt.title('Número de Empregados por Idade (Feminino)')
plt.xlabel('Idade')
plt.ylabel('Número de Empregados')
plt.show()

# Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade

agrupamento_cidade = mais_de_5_anos.groupby('City').agg({'JoiningYear':'count', 'ExperienceInCurrentDomain':'mean'}).reset_index()
agrupamento_cidade.columns = ['Cidade', 'Numero De Empregados', 'Media Experiencia']

# Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna LeaveOrNot do dataframe) Conte quantos empregados existem por PaymentTier

porcentagem_ainda_trabalhando = df_atualizado['LeaveOrNot'].mean() * 100

contagem_payment_tier = df_atualizado['PaymentTier'].value_counts()

# Substitua os valores da coluna EverBenched para True ou False

df['EverBenched'] = df['EverBenched'].map({'Yes': True, 'No': False})

# Crie um gráfico de pizza com o resultado da coluna EverBenched e outro com LeaveOrNot

resultado_everbenched = df['EverBenched'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(resultado_everbenched, labels=resultado_everbenched.index, autopct='%1.1f%%', colors=['Green', 'Red'])
plt.title('Distribuição de EverBenched (True/False)')
plt.show()

resultado_leaveornot = df['LeaveOrNot'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(resultado_leaveornot, labels=['0', '1'], autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
plt.title('Distribuição de LeaveOrNot (0/1)')
plt.show()