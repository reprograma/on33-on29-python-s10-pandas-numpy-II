import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../material/desenvolvimento_paises.csv")

# print(df.describe())
# print(df.info())
# # Fazer dentro de uma coluna específica
# print(df["AveragScore"].value_counts())

# Altera o df original. Para não alterar, não colocar o inplace
# print(df.fillna(value=0, inplace=True))
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df.drop_duplicates(inplace=True))
# print(df.duplicated().sum())

# country_greater_security_value = df["SafetySecurity"].max()
# country_lesser_security_value = df["SafetySecurity"].min()
# print(country_greater_security_value)
# print(country_lesser_security_value)
# print("A diferença entre o maior país com SafetySecurity é de: ", country_greater_security_value - country_lesser_security_value)

# line_higher_security_value = df[df["SafetySecurity"] == country_greater_security_value]
# print(line_higher_security_value)

# index_greater_value = df["SafetySecurity"].idxmax()
# print(df.loc[index_greater_value])

columns_name = df.columns
columns_name = columns_name.drop(labels="Country")

def categorizar_valores(valor):
    if valor > 80:
        return "Desenvolvido"
    if valor < 70 and valor >= 50:
        return "Em desenvolvimento"
    if valor < 60:
        return "Subdesenvolvido"
    else:
        return "Não categorizado"

df["Media"] = df[columns_name].mean(axis=1)
df["Categoria_Desenvolvimento"] = df["Media"].apply(categorizar_valores)

# print(df["Media"])
# print(df["Categoria_Desenvolvimento"].value_counts())

development_category_counts = df["Categoria_Desenvolvimento"].value_counts()
print(development_category_counts)

development_category_counts.plot(kind="bar", title="QTD Países por Categoria")
# plt.xticks(rotation=45)
# plt.show()

personel_freedom_filter = df.where((df["PersonelFreedom"] <= 30) & (df["Categoria_Desenvolvimento"] == "Subdesenvolvido"))

personel_freedom_filter.dropna(inplace=True)

print(personel_freedom_filter.info())