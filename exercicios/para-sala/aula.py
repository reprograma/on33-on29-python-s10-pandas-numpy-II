import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\git-on33\on33-python-s10-pandas-numpy-II\material\desenvolvimento_paises.csv")

# print(df.describe()) 
# print(df.info()) # traz informação de valores nao nulos por colunas e o tipo das colunas
# print(df["AveragScore"].value_counts()) # não aplicar em todo o dataframe e sim em uma coluna. Ele vai contar as linhas com valores iguais ex: tem duas linhas com valores 2 então 2.2

# print(df.isnull().sum()) # somar linhas nulas em cada colunas e mostrar
# df_sem_valores_nulos = df.fillna(0) # se usar o fillna sem inplace para salvar no dataframe novo para eu manipular
# print(df.fillna(value=0, inplace=True)) # inplace=true para modificar no dataframe para "0"
# print(df.isnull().sum())
# print(df.duplicated().sum()) # identificar linhas duplicadas para apagar
# print(df.drop_duplicates(inplace=True)) # inplace=true para modificar no dataframe original que eu chamei a função para "0"
# print(df.duplicated().sum())

# country_max_security_value = df["SafetySecurity"].max()
# # country_min_security_value = df["SafetySecurity"].min()
# print(country_max_security_value)
# # print(country_min_security_value)
# # print("A diferença entre o maior pais com SafetySecurity é de:",country_max_security_value - country_min_security_value)

# # # Encontra mais de uma linha onde o valor máximo esteja presente
# linha_maior_valor_security = df[df["SafetySecurity"] == country_max_security_value]
# print(linha_maior_valor_security)

# # # retornar o index do primeiro valor máximo encontrado
# index_greater_value = df["SafetySecurity"].idxmax()

# # retornar dados da linha por index
# print(df.loc[index_greater_value])

# excluir valores de uma lista/dimensão
columns_name = df.columns
columns_name = columns_name.drop( labels="Country")
print(columns_name)
df["Media"] = df[columns_name].mean(axis=1) # axis=1 aplicar em apenas uma linha/dimensão

print(df["Media"])
print(df.info())

def categorizar_valores(valor):
    if valor > 80:
        return  "Desenvolvido"
    if valor < 70 and valor >=50:
        return "Em Desenvolvimento"
    if valor < 60 :
        return "Subdenvolvido"
    else:
        return "Não Categorizado"
    
df["Categoria_Desenvolvimento"] = df["Media"].apply(categorizar_valores) # apply usar a def para categorizar a nova coluna criada

development_category_counts = df["Categoria_Desenvolvimento"].value_counts()

print(development_category_counts)

development_category_counts.plot(kind="bar", title="QTD Países por Categoria") # plotar o gráfico nesse caso
# vamos usar pensa o tipo e o título

# plt.show() # mostrar gráfico

# filtre os dados onde o PersoneFreedom seja inferior a 30, se exister. 
personel_freedom_filter = df.where(df["PersonelFreedom"] <= 30)

# mais de um filtro
# personel_freedom_filter = df.where((df["PersonelFreedom"] <= 30) & (df["Categoria_Desenvolvimento"] =="Desenvolvido"))

# apagar os na e deixar só com os filtro inferior a 30 que seja verdadeiro
personel_freedom_filter.dropna(inplace=True)

print(personel_freedom_filter.info())

# ordenação por colunas
print(df.sort_values(by=["Education", "Health"], inplace=True, ascending=True))
print(df.head())
