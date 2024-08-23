import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import datetime as dt

df = pd.read_csv(r"C:\Users\nada_\OneDrive\Desktop\REPROGRAMA\on33-python-s12-pandas-numpy-II\material\Employee.csv")

#Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos.
print(df.info()) #analisando valores nulos
print(df.drop_duplicates(inplace=True)) #exclusão de valores duplicados
print(df.duplicated().sum())

# Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.
maior_cinco_anos = df[df['ExperienceInCurrentDomain'] > 5] #coluna de experiencia no cargo
print(maior_cinco_anos)
maior_cinco_anos.to_csv("./FuncionariosExperientes.csv", index=False) #novo dataframe

# Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.
gender_employees = df["Gender"].value_counts()
age_employees = df["Age"].value_counts()

print(df["Gender"].value_counts())
print(df["Age"].value_counts())

gender_employees.plot(kind='barh', color='blue', title='Quantidade de Empregados por Gênero')
plt.ylabel('Gênero')
plt.xlabel('Número de Empregados')
plt.show()

age_employees.plot(kind='barh', color='green', title='Quantidade de Empregados por Idade')
plt.ylabel('Idade')
plt.xlabel('Número de Empregados')
plt.show()

# Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade

city_with_more_employees_number = df["City"].value_counts().values
city_with_more_employees_name = df["City"].value_counts().index
print(f"\n{city_with_more_employees_name[0]} is the city which has the highest number of employees with {city_with_more_employees_number[0]} employees")

current_year = datetime.now().year
average_per_city = df.groupby('City')['JoiningYear'].mean().apply(lambda x: current_year - x)
print('The average length of service is: ', average_per_city)

# Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)

total_employees = len(df)
working = df["LeaveOrNot"].value_counts()
working_percentage = (working / total_employees) * 100
print(f"A empresa possui cerca de {working_percentage[0]:.2f}% dos empregados.")

# Conte quantos empregados existem por `PaymentTier`.

payment_tier = df['PaymentTier'].value_counts()
print(payment_tier)

# Substitua os valores da coluna `EverBenched` para `True` ou `False`

df['EverBenched'] = df['EverBenched'].replace({'Yes': True, 'No': False})
print(df['EverBenched'].head()) 

# Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`
GrafEver = df['EverBenched'].value_counts()
GrafLeave = df['LeaveOrNot'].value_counts()

GrafEver.plot(kind='pie', autopct='%1.1f%%', title='EverBenched') # Gerando e imprimindo gráficos
plt.show()
GrafLeave.plot(kind="pie", autopct='%1.1f%%',title='LeaveOrNot') 
plt.show()



