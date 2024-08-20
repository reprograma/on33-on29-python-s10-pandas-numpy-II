import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('./employee.csv')
# print(df.info())
# print(df.describe())
# print(df.head())
# print(df.columns)
# ['Education', 'JoiningYear', 'City', 'PaymentTier', 'Age', 'Gender',
#        'EverBenched', 'ExperienceInCurrentDomain', 'LeaveOrNot']


#- Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos.

# print(df.isnull().sum())
 #sem valores nulos 

# print(df.drop_duplicates(inplace=True))
# print(df.duplicated().sum())


#- Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.

# mais_cinco_anos = df[df['ExperienceInCurrentDomain'] > 5]
# print(mais_cinco_anos)


# -Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.
#feminino_por_idade = df[df['Gender'] == 'Female']['Age'].value_counts().sort_index()
#rotulo = feminino_por_idade.plot(kind='bar', title='Quantidade de mulheres por idade')

#masculino_por_idade = df[df['Gender'] == 'Male']['Age'].value_counts().sort_index()
#rotulo = masculino_por_idade.plot(kind='bar', title='Quantidade de homens por idade')

# Adicionar rótulos nas barras de forma simplificada(usado IA para rotular as barras)
#rotulo.bar_label(ax.containers[0], label_type='edge', fontsize=10)

# Concatenar os dois dataframes para comparação 
# comparativo = pd.concat([feminino_por_idade, masculino_por_idade], axis=1)

# rotulo = comparativo.plot(kind='bar', figsize=(10, 6), color=['red', 'blue'])

# rotulo.set_title('Quantidade de Homens e Mulheres por Idade')
# rotulo.set_xlabel('Idade')
# rotulo.set_ylabel('Quantidade')
# rotulo.set_xticks(range(len(comparativo.index)))
# rotulo.set_xticklabels(comparativo.index, rotation=45)
# rotulo.legend(title='Gênero')

# Adicionar rótulos nas barras
# for container in rotulo.containers:
#     rotulo.bar_label(container, label_type='edge', fontsize=10)
# plt.tight_layout()
# plt.show()


# - Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade
# valores_unicos = df['City'].unique()# conferindo as cidades existentes
# print(valores_unicos)

# cidades = df['City'].value_counts().idxmax()
# print(' A cidade com mais empregados é: ', cidades)

# ano_atual = datetime.now().year
# media_cidade = df.groupby('City')['JoiningYear'].mean().apply(lambda x: ano_atual - x)

# print('a media do tempo de serviço em anos é: ', media_cidade)



#-Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)
#print (df['LeaveOrNot'].dtype)
# percentual_atual = (df['LeaveOrNot'].mean()) * 100
# print(f'Porcentagem de empregados que ainda trabalham na empresa: {percentual_atual:.2f}%')


#-Conte quantos empregados existem por `PaymentTier`

# qt_empregados = df['PaymentTier'].value_counts().sort_index()
# print(qt_empregados)


#-Substitua os valores da coluna `EverBenched` para `True` ou `False`
# df['EverBenched'] = df['EverBenched'].replace({'Yes': True, 'No': False})
# print(df['EverBenched'])


#-Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`

# df['EverBenched'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['red','blue'], title='Reservas')
# plt.show()


# contagem = df['LeaveOrNot'].value_counts()
# labels = ['Sim' if index == 1 else 'Não' for index in contagem.index] #IA 
# contagem.plot(kind='pie', autopct='%1.1f%%', colors=['blue', 'red'], labels=labels, title='Atualmente na Empresa?')
# plt.show()


