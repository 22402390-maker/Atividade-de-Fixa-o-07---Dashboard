import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_distribuicao = pd.read_csv("dados_distribuicao.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    data=df_distribuicao,
    x="idade",
    bins=10,
    kde=True,
    color="#2563eb",
    ax=ax
)

ax.set_title("Distribuição da Idade dos Clientes", fontweight="bold")
ax.set_xlabel("Idade")
ax.set_ylabel("Quantidade de Clientes")

plt.tight_layout()
plt.show()


'''
import matplotlib.pyplot as plt
import seaborn as sns

df_tips = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8, 4))

# Histograma com curva KDE (Kernel Density Estimation)
sns.histplot(
    data=df_tips, x="total_bill",
    bins=15, kde=True,
    color="#2563eb", ax=ax
)

ax.set_title("Distribuição dos Valores das Contas", fontweight="bold")
plt.tight_layout()
plt.show()
'''