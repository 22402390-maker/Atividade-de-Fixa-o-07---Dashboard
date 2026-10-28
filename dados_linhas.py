import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid")

df_dados_linhas = pd.read_csv("dados_linhas.csv")

df_dados_linhas["data"] = pd.to_datetime(df_dados_linhas["data"])

fig, ax = plt.subplots(figsize=(10, 4))

sns.lineplot(
    data=df_dados_linhas,
    x="data",
    y="vendas",
    marker="o",
    color="#2563eb",
    linewidth=2,
    ax=ax
)

ax.set_title("Evolução das Vendas", fontweight="bold")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


'''
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
df_flights = sns.load_dataset("flights")

fig, ax = plt.subplots(figsize=(10, 4))

# Criando o gráfico de linhas
sns.lineplot(
    data=df_flights[df_flights["year"] == 1960],
    x="month", y="passengers",
    marker="o", color="#2563eb", linewidth=2, ax=ax
)

ax.set_title("Evolução do Número de Passageiros (1960)", fontweight="bold")
ax.set_xlabel("Mês")
ax.set_ylabel("Total de Passageiros")

plt.tight_layout()
plt.show()
'''