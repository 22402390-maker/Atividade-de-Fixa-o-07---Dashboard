import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_dispersao = pd.read_csv("dados_dispersao.csv")

fig, ax = plt.subplots(figsize=(8, 4))

# Gráfico de dispersão + linha de regressão
sns.scatterplot(
    data=df_dispersao,
    x="altura_cm",
    y="peso_kg",
    hue="sexo",
    alpha=0.8,
    ax=ax
)

sns.regplot(
    data=df_dispersao,
    x="altura_cm",
    y="peso_kg",
    scatter=False,
    color="gray",
    ax=ax
)

ax.set_title("Relação entre Altura e Peso", fontweight="bold")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")

plt.tight_layout()
plt.show()


'''
import matplotlib.pyplot as plt
import seaborn as sns

df_tips = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8, 4))

# Scatter plot + Linha de Regressão
sns.scatterplot(
    data=df_tips, x="total_bill", y="tip",
    hue="time", alpha=0.8, ax=ax
)
sns.regplot(data=df_tips, x="total_bill", y="tip", scatter=False, color="gray", ax=ax)

ax.set_title("Relação entre Valor da Conta e Gorjeta", fontweight="bold")
plt.tight_layout()
plt.show()
'''