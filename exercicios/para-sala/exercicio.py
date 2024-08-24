import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\sanel\OneDrive\Área de Trabalho\git-on33\on33-python-s10-pandas-numpy-II\material\desenvolvimento_paises.csv")
# r muda a nossa string para reconher o patch  do arquivo.

# Esses  comando são chamados sumary
#print(df.describe()) # olha para o dataframe faz a descrição matemática por coluna numerica
#print(df.info()) # todos os dados da coluna, valores não nulos por coluna traz também o dtype, o tamanho do dataframe
#print(df.value_counts("AveragScore")) # Pode ser aplicado em todo o dataframe mas é indicado só aplica em uma coluna especifica e ele adiciona na quantidade os que são iguais pra todos os itens da coluna 

#print(df.isnull().sum()) # traz os valores nulos do dataframe, retorna false e true. Dependo do que for fazer utilizar e ver o que será coletado.
#print(df.fillna(0)) # Não altera o dataframe original 
#print(df.fillna(0, inplace=True)) # Cria outro dataframe sem alterar o dataframe original
#print(df.isnull().sum())
#print(df.duplicated().sum()) # traz uma serie com os valores duplicados
#print(df.drop_duplicates(inplace=True)) # so pode ser aplicado em um dataframe
#print(df.duplicated().sum())

#pais_max_security_value = df['SafetySecurity'].max()
#pais_min_security_value = df['SafetySecurity'].min()
#print(pais_max_security_value)
#print(pais_min_security_value)
#print("A diferença entre o maior pais com SafetySecurity é de:", pais_max_security_value - pais_min_security_value)

# Filtro retorna na minha linha safetysecurity é maior 
#linha_max_security_value = df[df['SafetySecurity']== pais_max_security_value] 
#print(linha_max_security_value['SafetySecurity'])

#index_greater_value = df['SafetySecurity'].idxmax() # retorna o primeiro valor máximo encontrato
#print(index_greater_value) # retorna o index só com o valor
#print(df.iloc[index_greater_value]) # loc ou i.loc retorna dados da linha por index


columns_name = df.columns   
columns_name = columns_name.drop(labels="Country") # exclui um valor de uma lista ou coluna expecifica, inplace modifica e preserva o original. Precisa verircar qual
#o tipo de drop para qual dataframe, no

#print(columns_name)

df["Média"] = df[columns_name].mean(axis=1) # aqui calcula a média das colunas em uma dimensão por isso o argumento axis =1, eixo x ou Y 

df["Categoria Desenvolvimento"] = df['Média'].apply(lambda valor: valor + 2) # aqui adiciona 2 no valor da média. Mas o apply pode ser usados em todas as operações mas o lambida é limitado a 2
print(df['Média'])
print(df.info())

#Se fizer o Apply.df aplica uma função em todo dataframe 
#lambda é uma função anomina e executada quando ela é chamada

print(df["Categoria Desenvolvimento"])

def categorizar_valores(valor): # aqui o valor é a média
    if valor > 80:
        return "Desenvolvido"
    if valor < 70 and valor >= 50:
        return "Em Desenvolvimento"
    if valor < 60:
        return "Subdesenvolvido"
    else:
        return "Não Categorizado"

df["Categoria Desenvolvimento"] = df["Média"].apply(categorizar_valores)
print(df["Categoria Desenvolvimento"])

print(df["Categoria Desenvolvimento"].value_counts()) # aqui foi apresentado a quantidade de quantos paises por categoria de desenvolvimento

development_category_counts = df["Categoria Desenvolvimento"].value_counts()

print(development_category_counts)

development_category_counts.plot(kind="bar", title="QTD Países por Categoria")

plt.show()
#Filtre os dados onde o PersonelFreedom seja inferior a 30. Se existir
#personel_freedom_filter = df.where((df["PersonelFreedom"] <= 30.0) & (df["Categoria Desenvolvimento"]== "Subdesenvolvido"))

#personel_freedom_filter.dropna(inplace=True)


#print(personel_freedom_filter.info())

#print(df.sort_values(by=["Education", "Health"], inplace=True, ascending=False))
#print(df.head())np.nan
