import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv(r"C:/Users/Colaborador/Reprograma/on33-python-s10-pandas-numpy-II/material/Employee.csv")

current_year = datetime.now().year  # Pegar o ano atual
df['YearsAtCompany'] = current_year - df['JoiningYear']

df = df.drop_duplicates()
gender_group = df.groupby('Gender').size()

print(gender_group)

gender_group.plot(kind='bar', title='Distribuição por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Número de Empregados')
plt.show()


age_group = df.groupby('Age').size()
print(age_group)

age_group.plot(kind='bar', title='Distribuição por Idade')
plt.xlabel('Idade')
plt.ylabel('Número de Empregados')
plt.show()

city_group = df.groupby('City').size()
print(city_group)

mean_service_time_by_city = df.groupby('City')['YearsAtCompany'].mean()
print(mean_service_time_by_city)

city_group.plot(kind='bar', title='Número de Empregados por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Número de Empregados')
plt.show()
