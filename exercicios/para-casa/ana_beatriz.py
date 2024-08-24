import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\anabi\OneDrive\Área de Trabalho\Git On33\Semana 12\on33-python-s10-pandas-numpy-II\material\Employee.csv")


print(df.info())
print(df.isnull().sum())


print(df.drop_duplicates(inplace=True))
print(df.duplicated().sum())


ano_atual = datetime.now().year
df['Anos de Serviço'] = ano_atual - df['JoiningYear']
df_mais_5_anos = df[df['Anos de Serviço'] > 5]
print(df_mais_5_anos.head())


generos_funcionarios = df["Gender"].value_counts()
idade_funcionarios = df["Age"].value_counts().sort_index()


generos_funcionarios.plot(kind='bar', figsize=(8, 6), color='skyblue', title= "Gênero dos funcionários")
plt.show()


idade_funcionarios.plot(kind='bar', figsize=(8, 6), color='skyblue', title= "Idade dos funcionários")
plt.show()


cidade_com_mais_empregados = df['City'].value_counts().idxmax()
print(f"A cidade com mais empregados é: {cidade_com_mais_empregados}")


media_tempo_servico_por_cidade = df.groupby('City')['Anos de Serviço'].mean()
print(media_tempo_servico_por_cidade)


total_empregados = len(df)


empregados_ativos = len(df[df['LeaveOrNot'] == 0])


porcentagem_ativos = (empregados_ativos / total_empregados) * 100


print(f"Porcentagem de empregados que ainda trabalham na empresa: {porcentagem_ativos:.2f}%")


contagem_tier = df['PaymentTier'].value_counts()
print(contagem_tier)


df['EverBenched'] = df['EverBenched'].apply(lambda x: True if x == 'Yes' else False)


print(df.head())


everbenched_counts = df['EverBenched'].value_counts()
leaveornot_counts = df['LeaveOrNot'].value_counts()


everbenched_counts.plot(kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightgreen', 'lightcoral'],
    figsize=(6, 6),
    title="Distribuição de EverBenched (True/False)"
)
plt.xlabel('')  
plt.grid(False)
plt.ylabel('')
plt.show()


plt.clf()


leaveornot_counts.plot(kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightgreen', 'lightcoral'],
    labels=['Ainda Trabalha', 'Deixou a Empresa'],
    figsize=(6, 6),
    title="Ainda Trabalha/Deixou a Empresa)",
)
plt.xlabel('')  
plt.grid(False)
plt.ylabel('')
plt.show()
