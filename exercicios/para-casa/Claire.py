import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv(r'C:\git-on33\on33-python-s10-pandas-numpy-II\material\Employee.csv')

# print(df.describe())
# print(df.info())

# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df.drop_duplicates(inplace=True))
# print(df.duplicated().sum())


#Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.
# funcionário com mais de 5 anos 
# Converter 'JoiningYear' para uma data completa assumindo 1º de janeiro

df["JoiningYear"] = pd.to_datetime(df["JoiningYear"].astype(str) + "-01-01")

# # Calculando o tempo de serviço em anos
hoje = datetime.now()

# dt.days extrai o número tota de dias da diferença calculada
df['YearsOfService'] = (hoje - df['JoiningYear']).dt.days / 365

# # Criando um DataFrame com empregados que trabalham há mais de 5 anos
employees_more_than_5_years = df[df['YearsOfService'] > 5]

print(employees_more_than_5_years)

# print(df.info())

#Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.
# size agrupa os dados por gênero e conta o número de ocorrências para cada gênero/age.
age_group = df.groupby('Age').size()
print(age_group)
age_group.plot(kind="bar", title="QTD idade")

plt.show()

gender_group = df.groupby('Gender').size()
print(gender_group)
gender_group.plot(kind="bar", title="QTD de Genero")

plt.show()


# #Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade
city_counts = df['City'].value_counts()
most_employees_city = city_counts.idxmax()
print(f'A cidade com o maior número de empregados é: {most_employees_city}')
print(city_counts)

 # Calculando a média do tempo de serviço dos empregados por cidade
average_service_by_city = df.groupby('City')['JoiningYear'].mean()
print("Média do tempo de serviço por cidade:")
print(average_service_by_city)

#Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna LeaveOrNot do dataframe)

total_employees = len(df)
still_employed_count = df[df['LeaveOrNot'] == 0].shape[0]
print(still_employed_count)

percentage_still_employed = (still_employed_count / total_employees) * 100
print(f'Porcentagem de empregados que ainda trabalham: {percentage_still_employed:.2f}%')

#Conte quantos empregados existem por PaymentTier

QTd_pay = df.groupby('PaymentTier').size()
print(QTd_pay)

#Substitua os valores da coluna EverBenched para True ou False
df['EverBenched'] = df['EverBenched'].replace({'Yes': True, 'No': False})
print(df['EverBenched'])

#Crie um gráfico de pizza com o resultado da coluna EverBenched e outro com LeaveOrNot

ever = df.groupby('EverBenched').size()
print(ever)
ever.plot(kind="pie", title="Yes/No", autopct="%1.0f")
plt.show()

stay_out = df.groupby('LeaveOrNot').size()
print(stay_out)
stay_out.plot(kind="pie",title="Stay/Out",autopct="%1.0f")
plt.show()

