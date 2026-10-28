import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_frequencia = pd.read_csv("dados_frequencia.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.countplot(
    data=df_frequencia,
    x="tipo_atendimento",
    hue="tipo_atendimento",
    palette="Set2",
    legend=False,
    ax=ax
)

ax.set_title("Frequência dos Tipos de Atendimento", fontweight="bold")
ax.set_xlabel("Tipo de Atendimento")
ax.set_ylabel("Quantidade de Chamados")

plt.tight_layout()
plt.show()