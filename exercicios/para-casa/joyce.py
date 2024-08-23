import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

df_empresa = pd.read_csv(r'C:\Users\55119\OneDrive\Área de Trabalho\REPROGRAMA (On33)\Semana12\on33-python-s10-pandas-numpy-II\material\Employee.csv')


# - Analise o dataset Employee e extraia as seguintes informações:
# - Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos.

print(df_empresa.info())
print(df_empresa.isnull().sum())
print(df_empresa.duplicated().sum())
print(df_empresa.drop_duplicates(inplace=True))
print(df_empresa.duplicated().sum())

# - Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.

ano = dt.datetime.now().year

df_empresa['tempo_empresa'] = (ano - df_empresa['JoiningYear'])
print(df_empresa)

cinco_anos = df_empresa[df_empresa['tempo_empresa'] > 5]
print(cinco_anos)

# - Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.

idade = df_empresa['Age'].value_counts()
genero = df_empresa['Gender'].value_counts()

idade.plot(kind='bar', title='Idade')
plt.show()

genero.plot(kind='bar', title='Gênero')
plt.show()

# - Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade

cidades = df_empresa['City'].value_counts()
mais_empregados = cidades.idxmax()
numero = cidades.max()
media_tempo = df_empresa.groupby('City')['tempo_empresa'].mean()

print(cidades)
print(f'Com {numero} empregados, a filial de {mais_empregados} é a cidade com mais colaboradores')
print('\nA média do tempo que os empregados trabalham na empresa é de ', media_tempo)

# - Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)

total_empregados = len(df_empresa)
atuando = df_empresa["LeaveOrNot"].value_counts()
porcentagem = (atuando / total_empregados) * 100
print(porcentagem)

# - Conte quantos empregados existem por `PaymentTier`

payment = df_empresa['PaymentTier'].value_counts()
print('A quantidade de empregados por: ')
print(payment)

# - Substitua os valores da coluna `EverBenched` para `True` ou `False`

df_empresa['EverBenched'] = df_empresa['EverBenched'].replace({'Yes': True, 'No': False})
print(df_empresa['EverBenched'].head())

# - Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`

benched = df_empresa['EverBenched'].value_counts()
leaveOrnot = df_empresa['LeaveOrNot'].value_counts()

benched.plot(kind= 'pie', title='EverBenched')
plt.show()
leaveOrnot.plot(kind='pie', title='LeaveOrNot')
plt.show()

