import pandas as pd

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

