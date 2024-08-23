import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv("/Users/laristch/Desktop/reprograma/on33-python-s10-pandas-numpy-II/material/Employee.csv")

# Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos.
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.
df_5_anos = df[df['ExperienceInCurrentDomain'] > 5]

# Agrupar empregados por gênero e idade
agrupado_genero_idade = df.groupby(['Gender', 'Age']).size()
print(agrupado_genero_idade)

# Gráfico de distribuição por gênero e idade
plt.hist(df[df['Gender'] == 'Male']['Age'], bins=10, alpha=0.5, label='Homens')
plt.hist(df[df['Gender'] == 'Female']['Age'], bins=10, alpha=0.5, label='Mulheres')

plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Distribuição de Idade por Gênero')
plt.legend(loc='upper right')
plt.show()

# Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade
cidade_com_mais_empregados = df['City'].value_counts().idxmax()
media_tempo_servico = df[df['City'] == cidade_com_mais_empregados]['ExperienceInCurrentDomain'].mean()
print(f"Cidade com mais empregados: {cidade_com_mais_empregados}")
print(f"Média de tempo de serviço em {cidade_com_mais_empregados}: {media_tempo_servico:.2f} anos")

# Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)
total_empregados = len(df)
empregados_na_empresa = df['LeaveOrNot'].value_counts()[0]
porcentagem_trabalham = (empregados_na_empresa / total_empregados) * 100
print(f"Porcentagem de empregados que ainda trabalham na empresa: {porcentagem_trabalham:.2f}%")

# Conte quantos empregados existem por `PaymentTier`
contagem_payment_tier = df['PaymentTier'].value_counts()
print("Contagem de empregados por PaymentTier:")
print(contagem_payment_tier)

# Substitua os valores da coluna `EverBenched` para `True` ou `False`
df['EverBenched'] = df['EverBenched'].replace({'No': False, 'Yes': True})

# Gráfico de pizza para EverBenched
df['EverBenched'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição de EverBenched')
plt.show()

# Gráfico de pizza para LeaveOrNot
df['LeaveOrNot'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição de LeaveOrNot')
plt.show()
