import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\GGGGGGG\Documents\Curso de Python\on33-python-s10-pandas-numpy-II\material\Employee.csv")
#print(df.head())
#print(df.columns) Printei as colunas do csv(['Education', 'JoiningYear', 'City', 'PaymentTier', 'Age', 'Gender','EverBenched', 'ExperienceInCurrentDomain', 'LeaveOrNot

#removi as linhas duplicadas
#df.drop_duplicates(inplace=True)
#print(df.duplicated().sum())

#Filtrar os empregados que têm mais de 5 anos de experiência
df_acima_de_5_anos = df[df["ExperienceInCurrentDomain"] > 5]
print(df_acima_de_5_anos)

# Agrupei por Gênero e Idade e contei o número de empregados em cada grupo
dados_agrupados = df_acima_de_5_anos.groupby(["Gender", "Age"]).size().reset_index(name='Count')
print(dados_agrupados)

#Criei o gráficos para cada gênero
genders = dados_agrupados["Gender"].unique()

for gender in genders:
    dados_filtrados = dados_agrupados[dados_agrupados["Gender"] == gender]
    
    plt.figure(figsize=(10, 5))
    plt.bar(dados_filtrados["Age"], dados_filtrados["Count"], color='skyblue')
    plt.xlabel('Idade')
    plt.ylabel('Número de Empregados')
    plt.title(f'Número de Empregados por Idade para o Gênero {gender}')
    plt.xticks(rotation=45)
    plt.show()

#Cod para o maior numero de empregados por cidade
cidade_empregados = df['City'].value_counts().idxmax()
print(f"A cidade com mais empregados é: {cidade_empregados}")

#Tempo de serviço por cidade
media_tempo = df.groupby('City')['ExperienceInCurrentDomain'].mean()
print("Média do tempo de serviço por cidade:")
print(media_tempo)

#porcentagem de funcionarios qu ainda trabalham
total_empregados = len(df)
empregados_trabalhando = df['LeaveOrNot'].value_counts().get(0, 0)  # ntendendo que 0 significa que ainda estão trabalhando

ainda_trabalhando = (empregados_trabalhando / total_empregados) * 100
print(f"Porcentagem de empregados ainda trabalhando na empresa: {ainda_trabalhando:.2f}%")

#Contagem de Empregados
contagem = df['PaymentTier'].value_counts()
print("Contagem de empregados por PaymentTier:")
print(contagem)

# Substituir os valores da coluna EverBenched
df['EverBenched'] = df['EverBenched'].replace({'Yes': True, 'No': False})
#print(df['EverBenched'].head())

# Criar o gráfico de pizza
experiencia = df['ExperienceInCurrentDomain'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(experiencia, labels=experiencia.index, autopct='%1.1f%%', startangle=140)
plt.title('Empregados por Tempo de Experiência')
plt.show()