import pandas as pd 
import matplotlib.pyplot as plt


# Carregar o DataFrame
df = pd.read_csv(r"C:\Users\bruno\Desktop\REPROG\on33-python-s10-pandas-numpy-II\material\Employee.csv")

# Verificar informações do DataFrame
print(df.info())

# Verificar e corrigir valores nulos
print("Valores nulos antes do preenchimento:")
print(df.isnull().sum())

df.fillna(0, inplace=True)  # Preencher valores nulos com 0
print("Valores nulos após o preenchimento:")
print(df.isnull().sum())

# Remover linhas duplicadas
df.drop_duplicates(inplace=True)
print("Número de duplicatas restantes:", df.duplicated().sum())

# Filtrar empregados com mais de 5 anos na empresa
df_more_than_5_years = df[df['ExperienceInCurrentDomain'] > 5]
print("Empregados com mais de 5 anos na empresa:")
print(df_more_than_5_years)

# Agrupar por gênero e contar o número de empregados
gender_counts = df['Gender'].value_counts()
gender_counts.plot(kind='bar', title='Número de Empregados por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Número de Empregados')
plt.show()

# Agrupar por faixa etária
age_bins = [20, 30, 40, 50, 60, 70]
age_groups = pd.cut(df['Age'], bins=age_bins)
age_counts = age_groups.value_counts().sort_index()
age_counts.plot(kind='bar', title='Número de Empregados por Faixa Etária')
plt.xlabel('Faixa Etária')
plt.ylabel('Número de Empregados')
plt.show()

# Encontrar a cidade com mais empregados
city_counts = df['City'].value_counts()
most_common_city = city_counts.idxmax()
print(f"A cidade com mais empregados é: {most_common_city}")

# Calcular a média do tempo de serviço por cidade
average_years_by_city = df.groupby('City')['ExperienceInCurrentDomain'].mean()
print("Média do tempo de serviço por cidade:")
print(average_years_by_city)

# Calcular a porcentagem de empregados que ainda trabalham na empresa
percentage_still_working = 100 * (df['LeaveOrNot'] == 0).mean()
print(f"Porcentagem de empregados que ainda trabalham na empresa: {percentage_still_working:.2f}%")

# Contar número de empregados por PaymentTier
payment_tier_counts = df['PaymentTier'].value_counts()
print("Número de empregados por PaymentTier:")
print(payment_tier_counts)

# Gráfico de pizza para a coluna "EverBenched"
ever_benched_counts = df['EverBenched'].value_counts()
ever_benched_counts.plot(kind='pie', autopct='%1.1f%%', title='Distribuição de EverBenched')
plt.ylabel('')  # Remove o rótulo do eixo y
plt.show()

# Gráfico de pizza para a coluna "LeaveOrNot"
leave_or_not_counts = df['LeaveOrNot'].value_counts()
leave_or_not_counts.plot(kind='pie', autopct='%1.1f%%', title='Distribuição de LeaveOrNot')
plt.ylabel('')  # Remove o rótulo do eixo y
plt.show()

