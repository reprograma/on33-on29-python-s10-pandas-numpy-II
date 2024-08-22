import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Lidi\Documents\{reprograma}\Git_on33\on33-python-s10-pandas-numpy-II\material\Employee.csv")

print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.drop_duplicates(inplace=True))
print(df.duplicated().sum())
print(df.info())
print(df.describe())

current_year = dt.date.today().year
five_years_ago = current_year - 5
filtered_df = df[(df["JoiningYear"] <= five_years_ago)]
print(filtered_df.describe())

df["Age"].value_counts().sort_index().plot(kind="barh", title="Empregados por Idade", xlabel="Quantidade", ylabel="Idades", color="goldenrod")
plt.show()

df["Gender"].value_counts().plot(kind="pie", title="Empregados por Gênero", colors=["lightpink", "lightskyblue"], autopct="%.2f%%")
plt.ylabel("")
plt.legend()
plt.show()

most_employees_city = df["City"].max()
print("A cidade com mais empregados é", most_employees_city)

df["LenghtService"] = current_year - df["JoiningYear"]
lenght_service_mean_by_city = df.groupby(["City"])["LenghtService"].mean()
print(lenght_service_mean_by_city)

total_employees = len(df)
not_working = df["LeaveOrNot"].value_counts()
not_working_pct = (not_working / total_employees) * 100
print(f"Em {current_year} cerca de {not_working_pct[0]:.2f}% dos empregados ainda trabalham na empresa.")

empolyees = len(df["PaymentTier"]) - not_working[1]
print(f"Atualmente existem {empolyees} empregados na empresa.")

def convertion(value):
    if value == "Yes":
        return True
    if value == "No":
        return False
    else:
        return "Não categorizado"

df["EverBenched"] = df["EverBenched"].apply(convertion)
print(df["EverBenched"])

# incluir a porcentagem na legenda e rótulo
df["EverBenched"].value_counts().plot(kind="pie", title="Empregados que já estiveram no banco", labels=["Não", "Sim"], colors=["peru", "sienna"], autopct="%.2f%%", explode=[0, 0.06])
plt.ylabel("")
plt.legend()
plt.show()

df["LeaveOrNot"].value_counts().plot(kind="pie", title="Empregados que já saíram da empresa", labels=["Permanecem na empresa", "Saíram da empresa"], colors=["seagreen", "lightgreen"], autopct="%.2f%%", explode=[0, 0.06])
plt.ylabel("")
plt.legend()
plt.show()