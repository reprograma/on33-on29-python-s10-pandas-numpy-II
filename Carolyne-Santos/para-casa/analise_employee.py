


#  - Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.
#  - Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.
#  - Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade
#  - Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)
#  - Conte quantos empregados existem por `PaymentTier`
#  - Substitua os valores da coluna `EverBenched` para `True` ou `False`
#  - Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`

## - Analise o dataset Employee e extraia as seguintes informações:
# Bibliotecas

import pandas as pd
import matplotlib.pyplot as plt

#Ler arquivo csv
df = pd.read_csv(r"C:\Users\carol\OneDrive\Área de Trabalho\Reprograma\on33-python-s12-pandas-numpy-II\material\Employee.csv")

#Visualizar meu df
print(df.head())
print(df.describe()) ##retornar informacoes descritivas do dataframe
print(df.info())   ##Retorna as informacoes de valores nulos por coluna e o dtype

##  - Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos.