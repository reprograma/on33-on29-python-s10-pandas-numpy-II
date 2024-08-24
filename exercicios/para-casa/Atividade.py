import pandas as pd
import datetime as dt  
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\brend\OneDrive\Documentos\PYTHON\REPROGRAMA\Semana 12\on33-python-s10-pandas-numpy-II\material\Employee.csv")

print(df.info())
print(df.isnull().sum())

#Listar soma das duplicadas
print(df.duplicated().sum())

#Excluir duplicadas e salvar
print(df.drop_duplicates(inplace=True))
print(df.duplicated().sum())

#Encontrar o ano atual
Ano_Atual = dt.datetime.now().year
print(Ano_Atual)

#Cálculo quantidade de anos na empresa
df["Tempo de Empresa"] = (Ano_Atual - df["JoiningYear"])
print(df.info())

#Filtro com os funcionários com mais de 5 anos
filtered_df = df[df["Tempo de Empresa"] > 5]
print(filtered_df.head())

#Salvando um novo DataFrame com os funcionários com mais de 5 anos
filtered_df.to_csv("./Funcionarios.csv", index=False)

#Agrupe os empregados por gênero e idade
Genero = df["Gender"].value_counts
print(Genero)
Idade = df["Age"].value_counts
print(Idade)

#crie um gráfico para cada caso acima
Genero.plot(kind="bar", title="Funcionários por Gênero")
plt.show()

Idade.plot(kind="bar", title="Funcionários por Idade")
plt.show()

#Veja qual a cidade que mais tem empregados
Cidades = df["City"].value_counts().idxmax()
print(Cidades)
Mais_funcionarios = df["City"].value_counts().max()
print(Mais_funcionarios)
print('A cidade com Mais funcionários é', Cidades, 'com', Mais_funcionarios, 'funcionários')

#faça uma média do tempo de serviço dos empregados por cidade
df["Tempo_servico"] = (Ano_Atual - df["JoiningYear"])
media_cidade = df.groupby("City")["Tempo_servico"].mean()
print(media_cidade)

#Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)
Funcionarios = df["LeaveOrNot"].count()
#print(Funcionarios)
Ativos = (df["LeaveOrNot"] > 0).sum()
Percentual = (Ativos / Funcionarios) * 100
print(format(round(Percentual,2)))

#Conte quantos empregados existem por `PaymentTier`
Qtdade_Funcionários = df['PaymentTier'].count()
print(Qtdade_Funcionários)

#Substitua os valores da coluna `EverBenched` para `True` ou `False`
df['EverBenched'] = df['EverBenched'].apply(lambda x: "False" if x == 'No' else "True")
print(df["EverBenched"])

#Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`
Grafico1 = df["EverBenched"].value_counts()
print(Grafico1)
Grafico1.plot(kind="pie")
plt.show()

Grafico2 = df["LeaveOrNot"].value_counts()
print(Grafico2)
Grafico2.plot(kind="pie")
plt.show()
