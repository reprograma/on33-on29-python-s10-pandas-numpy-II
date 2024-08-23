import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\flavi_000\OneDrive\Flavienne\Cursos\Reprograma\S12 - 17.08\on33-python-s10-pandas-numpy-II\material\desenvolvimento_paises.csv")

# print(df.describe()) # faz uma descrição matemát. dos dados, um resumo estatístico rápido de um DataFrame, media, desvio padrão, contagem de linhas em cada coluna
# print(df.info()) #fornece um resumo rápido e conciso das principais características numéricas dos seus dados
# print(df["AveragScore"].value_counts()) #aplicado apenas em uma coluna, mostra quantas vezes cada valor aparece nos seus dados.

# print(df.fillna(0, inplace=True))#o resultado deste dataframe será alterado no original
# print(df.isnull().sum()) #isnull() cria um DataFrame com a mesma forma que o original, mas com valores booleanos indicando onde há valores nulos.#sum() conta quantos valores True (nulos) há em cada coluna.usada para contar a quantidade de valores nulos (missing values) em cada coluna desse DataFrame
# print(df.duplicated().sum()) #calcula e retorna o número total de linhas duplicadas com true ou false presentes em um DataFrame.
# print(df.drop_duplicates(inplace=True))#deletar os valores duplicados
# print(df.duplicated().sum())#deletar os valores duplicados

#Item 2:Encontre os pais que têm o maior e o menor valor para a coluna SafetySecuritye imprima a diferença entre eles.  (alterar tudo p inglês depois)
# pais_maior_security_value = df["SafetySecurity"].max()
# pais_menor_security_value = df["SafetySecurity"].min()

# print(pais_maior_security_value)
# print(pais_menor_security_value)
# print("A diferença entre o maior país com SafetySecurity é de: ", pais_maior_security_value - pais_menor_security_value)

# #Encontra mais de uma linha onde o valor máximo esteja presente
# linha_maior_vaylor_security = df[df["SafetySecurity"] == pais_maior_security_value] #filtro, retorne as linhas desse dataframe
# print(linha_maior_vaylor_security)

# #outra forma de fazer o item 2:
# #retorna o index do primeiro valor máximo encontrado
index_greater_value = df["SafetySecurity"].idxmax()
# #retorna dados da linha por index
# print(df.iloc[index_greater_value])# o loc encontra dados na linha que vc escolheu

#Ativ 3: Use o apply() para criar uma coluna nova onde a média de todas as colunas - menos a Country- quando: Maior que 80 o valor seja "Desenvolvido", entre 50 e 70 seja "Em desenvolvimento" e menor que 60 seja "Subdesenvolvido"
# criar uma coluna nova
columns_name = df.columns

print(columns_name)
columns_name = columns_name.drop(labels= "Country") #deletando a coluna Country

df["Média"] = df[columns_name].mean(axis=1) #executa apenas na linha 1

def categorizar_valores(valor):
    if valor > 80:
        return "Desenvolvido"
    if valor < 70 and valor >=50:
        return "Em desenvolvimento"
    if valor < 60:
        return "Não Categorizado"
    
df["Categoria Desenvolvimento"] = df["Média"].apply(categorizar_valores)
#print(df["Categoria Desenvolvimento"])

development_category_counts = df["Categoria Desenvolvimento"].value_counts()

print(development_category_counts)

development_category_counts.plot(kind="bar", title="QTD Países por Categoria")

plt.show()
#Filtre os dados onde o PersonelFreedom seja inferior a 30. Se existir
personel_freedom_filter = df.where((df["PersonelFreedom"] <= 30) & (df["Categoria_Desenvolvimento"] == "Subdesenvolvido"))

personel_freedom_filter.dropna(inplace=True)

print(personel_freedom_filter.info())



