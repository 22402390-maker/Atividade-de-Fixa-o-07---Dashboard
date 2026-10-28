# Revisão — Gráficos com Python

Resumo dos principais gráficos feitos com **Pandas**, **Matplotlib** e **Seaborn**.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
```

- **Pandas** → lê e manipula os CSVs (`pd.read_csv("arquivo.csv")`)
- **Matplotlib** → cria e configura a figura (`plt.subplots`, `plt.show`)
- **Seaborn** → desenha os gráficos de forma simples

---

## Gráficos

| Gráfico | Serve para | Função | Arquivo |
|---|---|---|---|
| Linhas | Evolução ao longo do tempo | `sns.lineplot()` | `dados_linhas.csv` |
| Barras | Comparar categorias | `sns.barplot()` | `dados_barras.csv` |
| Dispersão | Relação entre duas variáveis | `sns.scatterplot()` | `dados_dispersao.csv` |
| Regressão | Linha de tendência | `sns.regplot()` | `dados_regressao.csv` |
| Boxplot | Distribuição, mediana e outliers | `sns.boxplot()` | `dados_boxplot.csv` |
| Heatmap | Intensidade em uma matriz | `sns.heatmap()` | `dados_heatmap.csv` |
| Pizza/Rosca | Proporção de um total | `ax.pie()` | `dados_pizza.csv` |
| Frequência | Contar categorias | `sns.countplot()` | `dados_frequencia.csv` |
| Histograma + KDE | Distribuição de números | `sns.histplot()` | `dados_distribuicao.csv` |

---

## Modelo base

```python
df = pd.read_csv("arquivo.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.barplot(data=df, x="coluna_x", y="coluna_y", ax=ax)  # troque pelo gráfico desejado

ax.set_title("Título", fontweight="bold")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")

plt.tight_layout()
plt.show()
```

### Parâmetros úteis

- `hue="coluna"` → separa por cor (ex.: região, sexo)
- `marker="o"` → pontos na linha
- `kde=True` e `bins=10` → curva e intervalos do histograma
- `annot=True` e `cmap="coolwarm"` → valores e cores do heatmap
- `autopct="%1.1f%%"` → porcentagens na pizza
- `wedgeprops=dict(width=0.6)` → transforma a pizza em rosca

---

## Como escolher o gráfico?

| Quero... | Use |
|---|---|
| Ver evolução no tempo | Linhas |
| Comparar categorias | Barras |
| Contar ocorrências | Countplot |
| Ver a distribuição de números | Histograma |
| Ver distribuição + outliers | Boxplot |
| Relacionar duas variáveis | Dispersão |
| Relação + tendência | Dispersão + regressão |
| Ver a porcentagem de um total | Pizza/Rosca |
| Ver valores em matriz | Heatmap |

> `barplot()` compara uma medida (ex.: média). `countplot()` conta quantas vezes cada categoria aparece.

---

## Fórmula mental

```text
CSV → pd.read_csv() → DataFrame → escolher gráfico → definir x e y → título/eixos → plt.show()
```