import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\lady_\OneDrive\Documentos\Reprograma-2024\reprograma\on33-python-s12-pandas-numpy-II\material\Employee.csv")

#- Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos.
print(df.isnull().sum()) #verificar se valores são nulos 
print(df.duplicated().sum()) #identidicar valores duplicados 
print(df.drop_duplicates(inplace=True))
print(df.duplicated().sum())

#- Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.
# Obtém o ano atual
current_year = pd.Timestamp.now().year  #Obtém o ano atual usando as funcionalidades de timestamp do Pandas.Timestamp é o equivalente pandas do Datetime do python e é intercambiável com ele na maioria dos casos

# Filtra os empregados que estão na empresa há mais de 5 anos
df_5_years = df[df['JoiningYear'] <= (current_year - 5)]
print(df_5_years)

#- Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.
grouped_gender = df.groupby('Gender')['Age'].count()
grouped_age = df.groupby('Age')['Gender'].count()

# Gráfico para gênero
grouped_gender.plot(kind='bar', color='purple', title='Número de Empregados por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Número de Empregados')
plt.show()

# Gráfico para idade
grouped_age.plot(kind='bar', color='green', title='Número de Empregados por Idade')
plt.xlabel('Idade')
plt.ylabel('Número de Empregados')
plt.show()

# - Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade

# cidade com mais empregados
cidade_com_mais_empregados = df['City'].value_counts().idxmax()
print(f"A cidade com mais empregados é: {cidade_com_mais_empregados}")

#Média do tempo de serviço por cidade
media_servico_por_cidade = df.groupby('City')['ExperienceInCurrentDomain'].mean()
print(media_servico_por_cidade)

#- Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)
# Calcular a porcentagem de empregados que ainda trabalham na empresa
percentagem_ativos = df['LeaveOrNot'].value_counts(normalize=True)[0] * 100   #O argumento normalize=True faz com que o value_counts() retorne as proporções em vez de contagens absolutas. Isso significa que os valores retornados serão frações ou percentagens (somando 1 ou 100%).
print(f"Percentual de empregados que ainda trabalham na empresa: {percentagem_ativos:.2f}%") 

#- Conte quantos empregados existem por `PaymentTier`
# Contar o número de empregados por PaymentTier
contagem_por_tier = df['PaymentTier'].value_counts()
print(contagem_por_tier)

#- Substitua os valores da coluna `EverBenched` para `True` ou `False`

df['EverBenched'] = df['EverBenched'].replace({'Yes': True, 'No': False})
print(df['EverBenched'].head())  # Verificar a substituição

#- Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`

# Gráfico de pizza para EverBenched

df['EverBenched'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Distribuição de EverBenched')
plt.show()

# Gráfico de pizza para LeaveOrNot
df['LeaveOrNot'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Distribuição de LeaveOrNot')
plt.show()


#print(df.fillna(0, inplace=True)) permite que altera, substituir valor 
#print(df.fillna(0)) #nesse dataframe subustiue com zero , não re recomendado obrveando data frame primeiro ,preencher valores nulos
#print(df.describe()) # vê data framfunção de summary, ele olha para nosso dataframe inteiro , analisa cada coluna e calcula de cada colunas os valores que são a tomas de todos os nivel. médiia por coluna numerico -gráfico 
#print(df.head()) # ve de forma normal o que tem no arquivo
#print(df.info()) # trás 3 informações , todos os nome das nossas colunas, contagem dos valores não nulos por colunas , ele tra´s também o Dtype (tipo), trás o tamanho do DataFrame
#print(df.duplicated())
#print(df["JoiningYear"].value_counts())
