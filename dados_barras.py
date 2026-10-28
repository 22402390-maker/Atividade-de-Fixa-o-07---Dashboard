import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_barras = pd.read_csv("dados_barras.csv")

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=df_barras,
    x="categoria",
    y="vendas_medias",
    hue="regiao",
    palette="Set2",
    errorbar=None,
    ax=ax
)

ax.set_title("Média de Vendas por Categoria e Região", fontweight="bold")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas Médias")
ax.legend(title="Região")

plt.tight_layout()
plt.show()


'''
import matplotlib.pyplot as plt
import seaborn as sns

df_tips = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8, 4))

# Gráfico de barras agregando média do valor total
sns.barplot(
    data=df_tips, x="day", y="total_bill",
    hue="sex", palette="Set2", errorbar=None, ax=ax
)

ax.set_title("Média do Valor da Conta por Dia e Gênero", fontweight="bold")
ax.set_ylabel("Média da Conta ($)")
ax.legend(title="Gênero")

plt.tight_layout()
plt.show()
'''