import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_pizza = pd.read_csv("dados_pizza.csv")

valores = df_pizza["faturamento"]
categorias = df_pizza["canal_venda"]
cores = sns.color_palette("Set2")

fig, ax = plt.subplots(figsize=(6, 6))

# Gráfico de Pizza / Rosca
ax.pie(
    valores,
    labels=categorias,
    autopct="%1.1f%%",
    startangle=90,
    colors=cores,
    wedgeprops=dict(width=0.6, edgecolor="white")
)

ax.set_title("Distribuição do Faturamento por Canal de Venda", fontweight="bold")

plt.tight_layout()
plt.show()

'''
import matplotlib.pyplot as plt
import seaborn as sns

valores = [40, 30, 20, 10]
categorias = ["Produto A", "Produto B", "Produto C", "Outros"]
cores = sns.color_palette("Set2")

fig, ax = plt.subplots(figsize=(6, 6))

# Gráfico de Pizza / Rosca nativo do Matplotlib
ax.pie(
    valores, labels=categorias, autopct="%1.1f%%",
    startangle=90, colors=cores,
    wedgeprops=dict(width=0.6, edgecolor="white") # Rosca
)

ax.set_title("Distribuição de Vendas por Categoria", fontweight="bold")
plt.tight_layout()
plt.show()
'''