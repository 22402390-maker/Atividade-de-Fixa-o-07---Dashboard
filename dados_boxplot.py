import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_boxplot = pd.read_csv("dados_boxplot.csv")

fig, ax = plt.subplots(figsize=(8, 4))

# Boxplot por departamento
sns.boxplot(
    data=df_boxplot,
    x="departamento",
    y="salario",
    palette="Pastel1",
    ax=ax
)

ax.set_title("Dispersão dos Salários por Departamento", fontweight="bold")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")

plt.tight_layout()
plt.show()


'''
import matplotlib.pyplot as plt
import seaborn as sns

df_tips = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(8, 4))

# Boxplot por categoria (caixa IQR e mediana)
sns.boxplot(
    data=df_tips, x="day", y="total_bill",
    palette="Pastel1", ax=ax
)

ax.set_title("Dispersão do Valor da Conta por Dia", fontweight="bold")
plt.tight_layout()
plt.show()
'''