import pandas as pd
import matplotlib.pyplot as plt

# Nomeando o df de employee
employee = pd.read_csv(r"C:\Users\sukzw\OneDrive\Documentos\reprograma\on33-python-s10-pandas-numpy-II\material\Employee.csv")

# Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos:
# print(employee.info())
# print(employee.describe())
employee_limpa = employee.drop_duplicates(keep="first")
# print(employee_limpa.info())

# Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos:
employee_maior_que_5_anos = employee_limpa[employee_limpa['ExperienceInCurrentDomain'] > 5]

# Agrupe os empregados por gênero e idade e crie um gráfico para cada caso:
# Gráfico por gênero
employee_limpa["Gender"].value_counts().plot(kind='bar', title="Empregados por gênero")
plt.xlabel("Gênero")
plt.ylabel("Número de Empregados")
plt.show()

# Gráfico por idade

employee_limpa["Age"].value_counts().plot(kind='bar', title="Empregados por idade")
plt.xlabel("Idade")
plt.ylabel("Número de Empregados")
plt.show()

# Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade

cidade_mais_empregados = employee_limpa["City"].value_counts().idxmax()
media_tempo = employee_limpa.groupby("City")["ExperienceInCurrentDomain"].mean()
print(f"Cidade com mais empregados: {cidade_mais_empregados}")
print("Média do tempo de serviço por cidade:")
print(media_tempo)

# Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna LeaveOrNot do dataframe)

contagem = employee_limpa["LeaveOrNot"].value_counts()
total_empregados = contagem.sum()
porcentagem_trabalhando = round((contagem / total_empregados) * 100, 2)
print(porcentagem_trabalhando)

# Conte quantos empregados existem por PaymentTier

empregados_payment_tier = employee_limpa["PaymentTier"].value_counts()
print("Contagem de empregados por PaymentTier:")
print(empregados_payment_tier)

# Substitua os valores da coluna EverBenched para True ou False

employee_limpa.loc[:, "EverBenched"] = employee_limpa["EverBenched"].apply(lambda x: True if x == "Yes" else False)

# Crie um gráfico de pizza com o resultado da coluna EverBenched e outro com LeaveOrNot

employee_limpa["EverBenched"].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("Ever Benched")
plt.show()

employee_limpa["LeaveOrNot"].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("LeaveOrNot")
plt.show()