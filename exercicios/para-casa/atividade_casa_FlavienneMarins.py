import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt  

#Carregando o dataframe
df = pd.read_csv(r"C:\Users\flavi_000\OneDrive\Flavienne\Cursos\Reprograma\S12 - 17.08\on33-python-s10-pandas-numpy-II\material\Employee.csv")

print(df.describe()) # faz uma descrição matemát. dos dados, um resumo estatístico rápido de um DataFrame, media, desvio padrão, contagem de linhas em cada coluna

# Atividade 1 - Faça a limpeza do seu dataframe excluindo linhas duplicadas ou preenchendo valores nulos.
print(df.isnull().sum()) # sem valores nulos, logo não há células vazias ou com valor ausentes.
print(df.duplicated().sum()) #imprimiu 1889 valores duplicados.
print(df.duplicated().value_counts()) # conferi a frequência dos duplicados(true 1889) e não duplicados (false 2764) 
df.drop_duplicates(inplace=True) # remover as duplicadas no DF e as alterações serão permanentes no DF.
print(df.duplicated().value_counts()) #verificar se a remoção foi eficiente, resultado nulo não é exibido.

# Atividade 2  - Crie um dataframe que tenha os empregados que trabalham na empresa a mais de 5 anos.
current_year = dt.datetime.now().year #armazena na variável a data atual (ano)
print(current_year)

df["Years_of_Service"] = (df["JoiningYear"] - current_year) #DF criado que receberá o cálculo da quantidade de anos na empresa
print(df.info())

filtered_df = df[df["Years_of_Service"] > 5] #Filtro com os funcionários com mais de 5 anos
print(filtered_df.head())

# Atividade 3- Agrupe os empregados por gênero e idade e crie um gráfico para cada caso.

df["Age"].value_counts().sort_index().plot(kind="barh", title="Idade dos Empregados", xlabel="Quantidade", ylabel="Idades", color="LightSlateGray")
#Calcula a frequência de cada idade na coluna "Age" do DF;ordenando em ordem crescente;
plt.show()

df["Gender"].value_counts().plot(kind="pie", title="Gênero dos Empregados", colors=["DarkBlue" , "MediumVioletRed" ], autopct="%.2f%%")
# Calcula a frequência de cada gênero aparece na coluna "Gender" do DF e gera um gráfico
plt.ylabel("") #limpa os eixos x e y do gráfico de barras, pois solicitei um gráfico de pizza.
plt.legend() #adiciona uma legenda de cores no gráfico
plt.show()

# Atividade 4 - Veja qual a cidade que mais tem empregados e faça uma média do tempo de serviço dos empregados por cidade
    #Cidade que mais tem empregados
most_employees_city = df["City"].value_counts().idxmax() #conta quantos funcionários existem em cada cidade e pega o nome da cidade que aparece mais vezes.
print("A cidade com mais empregados é", most_employees_city)

    #Média do tempo de serviço dos empregados por cidade
df["years_of_service"] = current_year - df["JoiningYear"] #calcula a quantidade de anos de serviço para cada funcionário e armazenando o resultado em uma nova coluna chamada "years_of_service".
avg_time_service_by_city = df.groupby("City")["years_of_service"].mean() #calcula a média de anos de serviço para cada cidade.
print(f"\nMédia de tempo de serviço dos empregados por cidade \n{avg_time_service_by_city}")

# Atividade 5 - Faça a porcentagem de quantos empregados ainda trabalham na empresa (use a coluna `LeaveOrNot` do dataframe)
total_employees = df["LeaveOrNot"].count() #conta o número de funcionários que deixaram e os que não deixaram a empresa, selecionando o maior número de cada.
still_working = df["LeaveOrNot"].value_counts().values[0] #número de funcionários que ainda estão trabalhando na empresa
percent_employees = still_working / total_employees * 100 #converte a proporção em uma porcentagem
print(f"\nA porcentagem de empregados que continuam trabalhando na empresa é de {percent_employees:.2f}%")

# Atividade 6 - Conte quantos empregados existem por `PaymentTier`
employees_paymentTier = df["PaymentTier"].count() #conta quantos funcionários estão em cada nível de pagamento e seleciona o maior entre eles.
print(f"\nO número de empregados é de {employees_paymentTier}\n")

# Atividade 7 - Substitua os valores da coluna `EverBenched` para `True` ou `False`
df["EverBenched"].replace({"Yes": True, "No": False}, inplace=True) #convertendo os valores 
print(df["EverBenched"].head())

# Atividade 8 - Crie um gráfico de pizza com o resultado da coluna `EverBenched` e outro com `LeaveOrNot`
everbenched_counts = df["EverBenched"].value_counts()
leaveornot_counts = df["LeaveOrNot"].value_counts()

##gráfico dos everbenched
labels = ["No", "Yes"] #labels é utilizado para melhorar o layout do gráfico.
everbenched_counts.plot(kind='pie', labels=labels, autopct='%1.1f%%', colors=['Gray', 'Indigo'], title='Funcionários Desligados da Empresa')
plt.show()

##gráfico dos Leave or Not
labels = ["Funcionários Presentes na Empresa", "Funcionários Desligados da Empresa"]
leaveornot_counts.plot(kind='pie', labels=labels, autopct='%1.1f%%', colors=['Gray', 'Indigo'], title='Funcionários Presentes e Desligados da Empresa')
plt.show()