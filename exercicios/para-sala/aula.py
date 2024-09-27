import pandas as pd
<<<<<<< HEAD

df = pd.read_csv(r"C:\Users\Colaborador\Reprograma\on33-python-s10-pandas-numpy-II\material\desenvolvimento_paises.csv")

#print(df.describe())
#print(df.info())
#print(df["AveragScore"].value_counts())

# print (df.fillna(0, inplace=True))
# print (df.isnull().sum())
# print (df.duplicated().sum())
# print (df.drop_duplicates(inplace=True))
# print (df.duplicated().sum())

# pais_maior_security_value = df["SafetySecurity"].max()
# pais_menor_security_value = df["SafetySecurity"].min()

# print(pais_maior_security_value)
# print(pais_menor_security_value)
# print("A diferença entre o maior pais com SafetySecurity é de:", pais_maior_security_value)

# print (pais_maior_security_value)
# print (pais_menor_security_value)
# print ("A diferença entre o maior pais com SafetySecurity é de: ", pais_maior_security_value)

# linha_maior_valor_security = df["SafetySecurity"]== pais_maior_security_value
# print (linha_maior_valor_security)

# index_greater_value = df["SafetySecurity"].idxmax()
# print(df.loc[index_greater_value])

=======
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Projetos\Reprograma\on33-python-s10-pandas-numpy-II\material\desenvolvimento_paises.csv")

print(df.describe())
print(df.info())
print(df["AveragScore"].value_counts())

print(df.fillna(0, inplace=True))
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.drop_duplicates(inplace=True))
print(df.duplicated().sum())

pais_maior_security_value = df["SafetySecurity"].max()
pais_menor_security_value = df["SafetySecurity"].min()

print(pais_maior_security_value)
print(pais_menor_security_value)
print("A diferença entre o maior pais com SafetySecurity é de:",pais_maior_security_value - pais_menor_security_value)

#Encontra mais de uma linha onde o valor máximo esteja presente
linha_maior_valor_security = df[df["SafetySecurity"]== pais_maior_security_value]
print(linha_maior_valor_security)

#retorna o index do primeiro valor máximo encontrado
index_greater_value = df["SafetySecurity"].idxmax()
#Retorna dados da linha por index
# print(df.loc[index_greater_value])

columns_name = df.columns

print(columns_name)
columns_name = columns_name.drop(labels="Country")

df["Média"] = df[columns_name].mean(axis=1)

def categorizar_valores(valor):
    if valor > 80:
        return "Desenvolvido"
    if valor < 70 and valor >= 50:
        return "Em Desenvolvimento"
    if valor < 60:
        return "Subdesenvolvido"
    else:
        return "Não Categorizado"


df["Categoria Desenvolvimento"] = df["Média"].apply(categorizar_valores)
# print(df["Categoria Desenvolvimento"])

development_category_counts = df["Categoria Desenvolvimento"].value_counts()

print(development_category_counts)

development_category_counts.plot(kind="bar", title="QTD Países por Categoria")

plt.show()
#Filtre os dados onde o PersonelFreedom seja inferior a 30. Se existir
personel_freedom_filter = df.where((df["PersonelFreedom"] <= 30.0) & (df["Categoria Desenvolvimento"]== "Subdesenvolvido"))

personel_freedom_filter.dropna(inplace=True)


print(personel_freedom_filter.info())

print(df.sort_values(by=["Education", "Health"], inplace=True, ascending=False))
print(df.head())np.nan
>>>>>>> 50041aaf1b397c4277ed53a9f9391bab6871415d
