import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\55119\OneDrive\Área de Trabalho\REPROGRAMA (On33)\Semana12\on33-python-s10-pandas-numpy-II\material\desenvolvimento_paises.csv")

#print(df.describe())

#print(df.info())

#print(df['Country'].value_counts())

print(df.fillna(0, inplace=True)) #substitui os valores nulos por algum número, nesse caso 0(zero); 
#você usa o inplace True pra substituir no DataFrame original.
#Se você não coloca como True (por padrão ele vem como False), mesmo que você faça o fillna, ele não vai substituir no DataFrame, é como se ele salvasse em outro DataFrame.
#Por isso você tem que dar esse comando pra ele mudar.

print(df.isnull().sum())

print(df.duplicated().sum()) #apresenta linhas duplicadas

print(df.drop_duplicates(inplace=True)) #
print(df.duplicated().sum())

pais_maior_security_value = df['SafetySecurity'].max()
pais_menor_security_value = df['SafetySecurity'].min()
print(pais_maior_security_value)
print(pais_menor_security_value)
print('A diferença entre o maior país com SafetySecurity é de:' , pais_maior_security_value - pais_menor_security_value)

#encontra mais de uma linha onde o valor maximo esteja presente
linha_maior_valor_security = df[df['SafetySecurity'] == pais_maior_security_value] #filtro dizendo que a coluna 'SafetySecurity' seja igual ao "pais maior"; ou seja, irá retornar a linha que será igual 
print(linha_maior_valor_security['SafetySecurity'])

index_greater_value = df['SafetySecurity'].idxmax() # retorna o index do primeiro valor maximo encontrado
print(df.loc[index_greater_value]) #(loc) retorna dados da linha por index

columns_name = df.columns
columns_name = columns_name.drop(labels='Country') #drop(de index) é apagar, aqui está pegando todo o data frame a apagando a coluna escolhida que foi Country
print(columns_name)

def categorizar_valores(valor): #função criada como (Lambda)
    if valor > 80:              #Lambda é uma função anônima que aceita somente uma instrução
        return 'Desenvolvido'
    if valor < 70 and valor >= 50:
        return 'Em desenvolvimento'
    if valor < 60:
        return 'Subdesenvolvido'
    else:
        return 'Não Categorizado'

df['Média'] = df[columns_name].mean(axis=1)

df['Categoria Desenvolvimento'] = df['Média'].apply(categorizar_valores) #apply aplica uma lógica em todas as linhas do df
print(df['Categoria Desenvolvimento'])

development_category_counts = df['Categoria Desenvolvimento'].value_counts()
print(development_category_counts)

development_category_counts.plot(kind='bar', title='QTD Países por Categoria') #cria o gráfico, kind é o tipo, title é titulo
plt.show() #para mostrar o gráfico pronto

personel_freedom_filter = df.where(df['PersonelFreedom'] <= 30)

personel_freedom_filter.dropna(inplace=True)
print(personel_freedom_filter.info())

print(df.sort_values(by=['Education', 'Health'], inplace=True, ascending=False))
print(df.head())


