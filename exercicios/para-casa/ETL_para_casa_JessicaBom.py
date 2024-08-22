import pandas as pd
import matplotlib.pyplot as plt
from datetime import date as dt

df = pd.read_csv(r"/Users/jessica/reprograma/on33-python-s10-pandas-numpy-II/material/Employee.csv")
# print(df.describe())



# 1 - Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos.
print(df.isnull().sum()) #não retornou valores nulos
# print(df.duplicated().sum()) #retornou 1889 valores duplicados. Achei muito, resolvi conferir com o value_counts abaixo
print(df.duplicated().value_counts())
df.drop_duplicates(inplace=True)
print(df.duplicated().value_counts())




# 2  - Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.
current_year = dt.today().year
cutting_time = 5
df_more_than_five_years = df[current_year - (df["JoiningYear"]) > cutting_time]
# print(df_more_than_five_years.sum())




# 3- Agrupe os empregados por gênero e idade
gender_employees = df["Gender"].value_counts()
age_employees = df["Age"].value_counts()




#4 - e crie um gráfico para cada caso.
##gráfico do gênero com barras horizontais
plt.style.use("ggplot") #Achei no medium um site com orientações pra formatar os gráficos e ele usa esse ggplot como estilo, usei também
gender_employees.plot(figsize=[10,6], kind="barh",fontsize=8, title="Employees by Gender", alpha=.6, color=["darkblue", "purple"], xlabel="Number of employees", ylabel="Gender")
plt.show()

##gráfico da idade com barras verticais
age_employees.sort_index().plot(figsize=[10,6], kind="bar", fontsize=8, color="lightblue", width=.9, title="Employees by Age", xlabel="Age of employees", ylabel="Number of employees")
plt.show()




# 5 - Veja qual a cidade que mais tem empregados
city_with_more_employees_number = df["City"].value_counts().values
city_with_more_employees_name = df["City"].value_counts().index
# print(city_with_more_employees_name, city_with_more_employees_number)
print(f"\nThe city with more employees is {city_with_more_employees_name[0]} with {city_with_more_employees_number[0]} employees")




# 6 - e faça uma média do tempo de serviço dos empregados por cidade
df["years_of_service"] = current_year - df["JoiningYear"]
avg_time_service_by_city = df.groupby("City")["years_of_service"].mean()
print(f"\nSeguem as médias de tempo de serviço dos empregados por cidade \n{avg_time_service_by_city}")




#7 - Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)
total_employees = df["LeaveOrNot"].count()
still_working = df["LeaveOrNot"].value_counts().values[0]
percent_employees = still_working / total_employees * 100
print(f"\nA porcentagem de empregados que continuam trabalhando na empresa é de {percent_employees:.2f}%")




# 8 - Conte quantos empregados existem por `PaymentTier`
employees_paymentTier = df["PaymentTier"].count()
print(f"\nO número de empregados é de {employees_paymentTier}\n")




# 9 - Substitua os valores da coluna `EverBenched` para `True` ou `False`
df["EverBenched"].replace({"Yes": True, "No": False}, inplace=True)
# print(df["EverBenched"].head())




#10 - Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`
everbenched_counts = df["EverBenched"].value_counts()
leaveornot_counts = df["LeaveOrNot"].value_counts()

##gráfico dos everbenched
labels = ["No", "Yes"] #denominei as labels porque queria que aparecesse mais bonitinho no gráfico do que só com True ou False
everbenched_counts.plot(kind='pie', labels=labels, autopct='%1.1f%%', colors=['#66c2a5', '#fc8d62'], title='Employees EverBrenched')
plt.show()

##gráfico dos Leave or Not
labels = ["Still in company", "Leave the company"]
leaveornot_counts.plot(kind='pie', labels=labels, autopct='%1.1f%%', colors=['#66c2a5', '#fc8d62'], title='Employees that Leave or Still in the Company')
plt.show()

#OBS: nos gráficos de pizza usei o auxílio do chatGPT pra formatar mais legal e colocar os rótulos aparecendo (com esse autopct)