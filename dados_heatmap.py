import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_heatmap = pd.read_csv("dados_heatmap.csv")

matriz_clientes = df_heatmap.pivot(
    index="dia_semana",
    columns="horario",
    values="movimento_clientes"
)

fig, ax = plt.subplots(figsize=(10, 5))

# Heatmap do movimento de clientes
sns.heatmap(
    matriz_clientes,
    annot=True,
    fmt=".0f",
    cmap="coolwarm",
    linewidths=.5,
    ax=ax
)

ax.set_title("Movimento de Clientes por Dia e Horário", fontweight="bold")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da Semana")

plt.tight_layout()
plt.show()

'''
import matplotlib.pyplot as plt
import seaborn as sns

df_tips = sns.load_dataset("tips")
matriz_corr = df_tips.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(8, 4))

# Heatmap da matriz de correlação 2D
sns.heatmap(
    matriz_corr, annot=True, fmt=".2f",
    cmap="coolwarm", linewidths=.5, ax=ax
)

ax.set_title("Matriz de Correlação Numérica", fontweight="bold")
plt.tight_layout()
plt.show()
'''