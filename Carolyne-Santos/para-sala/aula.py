#Biblioteca
import pandas as pd
import matplotlib.pyplot as plt

#Ler arquivo csv (r)=rowdata
df = pd.read_csv(r"C:/Users/carol/OneDrive/Área de Trabalho/Reprograma/on33-python-s12-pandas-numpy-II/material/desenvolvimento_paises.csv")

#Visualizar meu df
print(df.describe()) ##retornar informacoes descritivas do dataframe
print(df.info())   ##Retorna as informacoes de valores nulos por coluna e o dtype

#Visualizar repetidos
print(df["AveragScore"].value_counts()) ##informar se ha valores repetidos, ou a quantidade de valores que existem de um determinado intervalo

#Limpeza dos dados
#preencher os valores nulos com zero
print(df.fillna(0, inplace=True))
#retorna todos os valores nulos das colunas do df
print(df.isnull().sum())
#retorna todos os valores duplicados nas colunas do df
print(df.duplicated().sum())
#Exclui os valores duplicados
print(df.drop_duplicates(inplace=True))
#Verifica do df apos a exclusao dos dados duplicados
print(df.duplicated().sum())

#criei um variavel para identificar o pais mais seguro conforme coluna 'SafetySecurity'
pais_maior_security_value = df["SafetySecurity"].max()
#criei um variavel para identificar o pais menos seguro conforme coluna 'SafetySecurity'
pais_menor_security_value = df["SafetySecurity"].min()

#retorna o valor da variavel criada acima
print(pais_maior_security_value)
print(pais_menor_security_value)
#retorna a diferenca entre o pais mais seguro e o menos seguro
print("A diferença entre o maior pais com SafetySecurity é de:",pais_maior_security_value - pais_menor_security_value)


#Encontra mais de uma linha onde o valor máximo esteja presente
linha_maior_valor_security = df[df["SafetySecurity"]== pais_maior_security_value]
print(linha_maior_valor_security)


#retorna o index do primeiro valor máximo encontrado
index_greater_value = df["SafetySecurity"].idxmax()
#Retorna dados da linha por index
print(df.loc[index_greater_value])

#Funcao para criar uma lista com todas as colunas do nosso df
columns_name = df.columns
print(columns_name)

#Chamei a funcao e utilizei 'drop' para excluir a coluna 'Country'
columns_name = columns_name.drop(labels="Country")
print(columns_name)

#Nova coluna para calculo da media de todas as colunas apos a exclusao da coluna 'Country'
df["Média"] = df[columns_name].mean(axis=1)

#funcao que categoriza as medias calculadas acima.
def categorizar_valores(valor):
    if valor > 80:
        return "Desenvolvido"
    if valor < 70 and valor >= 50:
        return "Em Desenvolvimento"
    if valor < 60:
        return "Subdesenvolvido"
    else:
        return "Não Categorizado"
    
# Nova coluna que guarda a resposta da funcao 'categorizar_valores'  
df["Categoria Desenvolvimento"] = df["Média"].apply(categorizar_valores) ## posso usar tbm (lambda), para executar a funcao assim que ela for definida.
#Verificar coluna
#print(df["Categoria Desenvolvimento"])

#Funcao que retorna a quantidade de categorias presente na coluna 'Categoria Desenvolvimento'
development_category_counts = df["Categoria Desenvolvimento"].value_counts()
#Verificar a funcao acima
print(development_category_counts)

#Grafico de barras com as quantidade de pais por categoria
development_category_counts.plot(kind="bar", title="QTD Países por Categoria")

#development_category_counts.plot(kind="pie", title="QTD Países por Categoria") ## grafico de pizza
#development_category_counts.plot(kind="barh", title="QTD Países por Categoria") ## grafico de barras na horizontal
#development_category_counts.plot(kind="line", title="QTD Países por Categoria") ## grafico de linha
# plt.xlabel('Categorias') ##titulos do eixo x
# plt.ylabel('Quantidade') ##titulos do eixo y
# plt.xticks('rotation=0') ##titulos do eixo vao ter rotacao = a 0

#Mostrar o grafico
plt.show()
#plt.savefig('grafico.png')  ##para salvar automaticamente o grafico

#Filtre os dados onde o 'PersonelFreedom' seja inferior a 30. Se existir
personel_freedom_filter = df.where((df["PersonelFreedom"] <= 30.0) & (df["Categoria Desenvolvimento"]== "Subdesenvolvido"))

#Excluir nulos ou NAN para retornar um df somente com o filtro que eu apliquei, ou seja menor que 30.0.
personel_freedom_filter.dropna(inplace=True)

#Visualizar a df com a funcao filtro aplicada
print(personel_freedom_filter.info())

#ordenar meu df por duas colunas "Education", "Health"
print(df.sort_values(by=["Education", "Health"], inplace=True, ascending=False)) ##Ordenando meu df do maior ao menor das colunas selecionadas
print(df.head())
