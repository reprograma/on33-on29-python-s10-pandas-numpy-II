#-----------------------------------------------------------------------------------------
# - Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos.
#-----------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

df = pd.read_csv("../../material/Employee.csv")

print(df.info())
print(df.isnull().sum()) #soma dos nulos
print(df.duplicated().sum()) #soma dos duplicados
df.drop_duplicates(inplace = True) #remoção dos duplicados
print(df.duplicated().sum()) #validação se todos foram removidos

#-----------------------------------------------------------------------------------------
# - Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.
#-----------------------------------------------------------------------------------------
# print(df.head())
# print(df.columns)

CurrentDate = date.today() #data atual
CurrentYear = int(CurrentDate.strftime("%Y")) #ano atual

df['CompanyTime'] = CurrentYear - df['JoiningYear']
funcionarios_df = df[df['CompanyTime'] >= 5]
print(funcionarios_df)

#-----------------------------------------------------------------------------------------
# - Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.
#-----------------------------------------------------------------------------------------

gender = df['Gender'].value_counts()
gender.plot(kind='barh', title='Employees Gender Graphy',color=['darkcyan', 'mediumpurple'])
plt.xlabel('Total Employees')
plt.show()

age = df['Age'].value_counts()
age.plot(kind='bar', title='Employees Age Graphy', color='mediumpurple')
plt.ylabel('Total Employees')
plt.show()

#-----------------------------------------------------------------------------------------
# - Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade
#-----------------------------------------------------------------------------------------

city_count = df['City'].value_counts()
city_max = city_count.idxmax()

MeanCompanyTime = df.groupby('City')['CompanyTime'].mean()
print(f'The city with the most employees is: {city_max}\n The mean of company time per city is:\n', MeanCompanyTime)

#-----------------------------------------------------------------------------------------
# - Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)
#-----------------------------------------------------------------------------------------

NoLeaveCount = (df['LeaveOrNot']== 0).sum()
LeaveCount = (df['LeaveOrNot'] == 1).sum()

Per_LeaveCount = (NoLeaveCount * 100) / len(df)
print(f'The percentage of employees who still work at the company is: {Per_LeaveCount:.1f}%')

#-----------------------------------------------------------------------------------------
# - Conte quantos empregados existem por `PaymentTier`
#-----------------------------------------------------------------------------------------

PaymentTierCount = df['PaymentTier'].value_counts()
print(PaymentTierCount)

#-----------------------------------------------------------------------------------------
# - Substitua os valores da coluna `EverBenched` para `True` ou `False`
#-----------------------------------------------------------------------------------------

df['EverBenched'] = df['EverBenched'].replace({'No':'False', 'Yes':'True'})
print(df['EverBenched'])

#-----------------------------------------------------------------------------------------
# - Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`
#-----------------------------------------------------------------------------------------

EverBenchedCount = df['EverBenched'].value_counts()
EverBenchedCount.plot(kind='pie',  title = 'Ever Benched Graphy', autopct='%1.1f%%', startangle=50, explode=(0,0.1), colors=['mediumpurple', 'darkcyan'])
plt.ylabel('')
plt.show()

df['LeaveOrNot'] = df['LeaveOrNot'].replace({0:'False', 1:'True'})
LeaveOrNotCount = df['LeaveOrNot'].value_counts()
LeaveOrNotCount.plot(kind='pie',  title = 'Leave Or Not Graphy', autopct='%1.1f%%', startangle=70, explode=(0,0.1), colors=['mediumpurple', 'darkcyan'])
plt.ylabel('')
plt.show()