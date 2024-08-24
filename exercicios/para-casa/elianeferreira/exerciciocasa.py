import pandas as pd
from datetime import datetime

import matplotlib.pyplot as plt



df = pd.read_csv(r"C:\Users\sanel\OneDrive\Área de Trabalho\git-on33\on33-python-s10-pandas-numpy-II\exercicios\para-casa\elianeferreira\Employee.csv")

#excluindo linhas duplicadas - drop_duplicates
#ou preenchendo valores nulos - df.fillna

#print(df.describe())
#print(df.info())
#print(df.isnull().sum())
#print(df.duplicated().sum())
#print(df.fillna(0))
#print(df.fillna(0, inplace=True))
print(df.duplicated().sum()) 
print(df.drop_duplicates().sum())
print(df.drop_duplicates(inplace=True))
print(df.duplicated().sum())
print(df.info())

#Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.
# - Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.

employee_for_five_years = df[df["ExperienceInCurrentDomain"]>5] 
print(employee_for_five_years)

group_gender = df.groupby(['Gender' , 'Age']).size().reset_index(name="Count")# não consegui evoluir nessa linha e renderizar o gráfico

#Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade

city_max_employee_value = df['City'].value_counts().idxmax()
print(city_max_employee_value)

mean_experience_city= df.groupby('City')['ExperienceInCurrentDomain'].mean().reset_index
print(mean_experience_city)

#Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)

employee_jobs = len(df)
still_working = len(df[df['LeaveOrNot']== 0])
percentage_employee_jobs= still_working/employee_jobs *100

print(percentage_employee_jobs)

 #Conte quantos empregados existem por `PaymentTier`
employee_for_payymentTier = df["PaymentTier"].value_counts()
print(employee_for_payymentTier)

#Substitua os valores da coluna `EverBenched` para `True` ou `False`

df["EverBenched"] = df['EverBenched'].replace({'Yes' : True , 'No' : False })

print(df)

#Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`- Essa linha do código não consegui renderizar
