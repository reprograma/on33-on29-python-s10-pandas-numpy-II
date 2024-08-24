import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\biamo\OneDrive\Área de Trabalho\git-on33\On33-S12\on33-python-s10-pandas-numpy-II\material\desenvolvimento_paises.csv')

# print(df.describe())
# print(df.info())
# print(df['AveragScore'].value_counts())


# print(df.fillna(0, inplace=True)) #substituindo todos os valores vazios (fill na) por 0.
# # O inplace = True modifica o dataframe
# print(df.isnull().sum()) #só o df.isnull mostra todos os dados com True pra nulo e False pra nao nulo, o sum resume isso.
# print(df.duplicated().sum())
# print(df.drop_duplicates(inplace=True))
# print(df.duplicated().sum())


# EXERCICIO DE AULA
paisMaior_securityValue = df['SafetySecurity'].max()
print(paisMaior_securityValue)

paisMenor_securityValue = df['SafetySecurity'].min()
print(paisMenor_securityValue)

print(f'A diferença entre o maior e menor país com SafetySecurity é: {paisMaior_securityValue - paisMenor_securityValue}')

# Encontra todas as linhas onde o valor maximo esteja presente
linha_paisMaiorValor = df[df['SafetySecurity'] == paisMaior_securityValue]
print(linha_paisMaiorValor['SafetySecurity'])

#Encontra a primeira linha que obtiver o valor maximo.
index_GreaterValue = df['SafetySecurity'].idxmax()
# Retornando a primeira linha com valor maximo em formato de index
print(df.loc[index_GreaterValue])

columnsName = df.columns
print(columnsName)

columnsName = columnsName.drop(labels='Country')

df['Média'] = df[columnsName].mean(axis=1)

def categorizarValores(valor):
    if valor > 80:
        return 'Desenvolvido'
    if valor < 70 and valor >= 50:
        return 'Em desenvolvimento'
    if valor < 60:
        return 'Subdesenvolvido'
    else:
        return 'Não categorizado'
    
df['Categoria Desenvolvimento'] = df['Média'].apply(categorizarValores)

developmentCategoryCounts = df['Categoria Desenvolvimento'].value_counts()

print(developmentCategoryCounts)

developmentCategoryCounts.plot(kind='bar', title='Qtde países por Categoria')

plt.show()

personelFreedomFilter = df.where((df['PersonelFreedom'] <= 30.0) & (df['Categoria Desenvolvimento'] == 'Subdesenvolvido'))

personelFreedomFilter.dropna(inplace=True)


print(personelFreedomFilter.info())

print(df.sort_values(by=['Education', 'Health'], inplace=True, ascending=False))
print(df.head())