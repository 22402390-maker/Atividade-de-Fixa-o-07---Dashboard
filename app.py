"""
Dashboard - Atividade de Fixação 07
Execute com:  streamlit run app.py
Coloque este arquivo na mesma pasta dos arquivos dados_*.csv.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Dashboard - Atividade 07",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

PASTA = Path(__file__).parent

ALUNO = {
    "Nome": "Rafael Vieira Gozaga",
    "Número da chamada": "34",
    "Turma": "2d2",
}

with st.sidebar:
    st.header("👤 Informações do aluno")
    for campo, valor in ALUNO.items():
        st.markdown(f"**{campo}:** {valor}")
    st.divider()
    st.caption("Atividade de Fixação 07 – Dashboard")


@st.cache_data
def carregar(nome: str) -> pd.DataFrame:
    return pd.read_csv(PASTA / nome)


sns.set_theme(style="whitegrid")
FIG = (5.5, 3.8)


def grafico_linhas():
    df = carregar("dados_linhas.csv")
    df["data"] = pd.to_datetime(df["data"])
    fig, ax = plt.subplots(figsize=FIG)
    sns.lineplot(data=df, x="data", y="vendas", marker="o",
                 color="#2563eb", linewidth=2, ax=ax)
    ax.set_title("Evolução das Vendas", fontweight="bold")
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig


def grafico_barras():
    df = carregar("dados_barras.csv")
    fig, ax = plt.subplots(figsize=FIG)
    sns.barplot(data=df, x="categoria", y="vendas_medias", hue="regiao",
                palette="Set2", errorbar=None, ax=ax)
    ax.set_title("Média de Vendas por Categoria e Região", fontweight="bold")
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Vendas Médias")
    ax.tick_params(axis="x", rotation=30)
    ax.legend(title="Região", fontsize=7, title_fontsize=8)
    fig.tight_layout()
    return fig


def grafico_pizza():
    df = carregar("dados_pizza.csv")
    fig, ax = plt.subplots(figsize=FIG)
    ax.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%",
           startangle=90, colors=sns.color_palette("Set2"),
           wedgeprops=dict(width=0.6, edgecolor="white"))
    ax.set_title("Faturamento por Canal de Venda", fontweight="bold")
    fig.tight_layout()
    return fig


def grafico_distribuicao():
    df = carregar("dados_distribuicao.csv")
    fig, ax = plt.subplots(figsize=FIG)
    sns.histplot(data=df, x="idade", bins=10, kde=True, color="#2563eb", ax=ax)
    ax.set_title("Distribuição da Idade dos Clientes", fontweight="bold")
    ax.set_xlabel("Idade")
    ax.set_ylabel("Quantidade de Clientes")
    fig.tight_layout()
    return fig


def grafico_boxplot():
    df = carregar("dados_boxplot.csv")
    fig, ax = plt.subplots(figsize=FIG)
    sns.boxplot(data=df, x="departamento", y="salario", hue="departamento",
                palette="Pastel1", legend=False, ax=ax)
    ax.set_title("Dispersão dos Salários por Departamento", fontweight="bold")
    ax.set_xlabel("Departamento")
    ax.set_ylabel("Salário (R$)")
    fig.tight_layout()
    return fig


def grafico_frequencia():
    df = carregar("dados_frequencia.csv")
    fig, ax = plt.subplots(figsize=FIG)
    sns.countplot(data=df, x="tipo_atendimento", hue="tipo_atendimento",
                  palette="Set2", legend=False, ax=ax)
    ax.set_title("Frequência dos Tipos de Atendimento", fontweight="bold")
    ax.set_xlabel("Tipo de Atendimento")
    ax.set_ylabel("Quantidade de Chamados")
    ax.tick_params(axis="x", rotation=20)
    fig.tight_layout()
    return fig


def grafico_dispersao():
    df = carregar("dados_dispersao.csv")
    fig, ax = plt.subplots(figsize=FIG)
    sns.scatterplot(data=df, x="altura_cm", y="peso_kg", hue="sexo",
                    alpha=0.8, ax=ax)
    sns.regplot(data=df, x="altura_cm", y="peso_kg", scatter=False,
                color="gray", ax=ax)
    ax.set_title("Relação entre Altura e Peso", fontweight="bold")
    ax.set_xlabel("Altura (cm)")
    ax.set_ylabel("Peso (kg)")
    fig.tight_layout()
    return fig


def grafico_regressao():
    df = carregar("dados_regressao.csv")
    fig, ax = plt.subplots(figsize=FIG)
    sns.scatterplot(data=df, x="renda_mensal", y="gasto_mensal",
                    alpha=0.8, ax=ax)
    sns.regplot(data=df, x="renda_mensal", y="gasto_mensal", scatter=False,
                color="gray", ax=ax)
    ax.set_title("Relação entre Renda e Gasto Mensal", fontweight="bold")
    ax.set_xlabel("Renda Mensal (R$)")
    ax.set_ylabel("Gasto Mensal (R$)")
    fig.tight_layout()
    return fig


def grafico_heatmap():
    df = carregar("dados_heatmap.csv")
    ordem = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    matriz = df.pivot(index="dia_semana", columns="horario",
                      values="movimento_clientes").reindex(ordem)
    fig, ax = plt.subplots(figsize=FIG)
    sns.heatmap(matriz, annot=True, fmt=".0f", cmap="coolwarm",
                linewidths=.5, annot_kws={"size": 7}, ax=ax)
    ax.set_title("Movimento de Clientes por Dia e Horário", fontweight="bold")
    ax.set_xlabel("Horário")
    ax.set_ylabel("Dia da Semana")
    fig.tight_layout()
    return fig


LINHAS = [
    {
        "titulo": "Vendas e faturamento",
        "graficos": [grafico_linhas, grafico_barras, grafico_pizza],
        "analise": (
            "**Evolução das vendas:** as vendas diárias de janeiro a março de 2026 "
            "mostram tendência de crescimento. A média dos primeiros 30 dias foi de "
            "cerca de 122, contra aproximadamente 226 nos últimos 30 dias. O menor "
            "valor foi 93,21 (14/01) e o maior, 260,37 (24/03).\n\n"
            "**Vendas por categoria e região:** a região Oeste tem a maior média "
            "(≈ 225), enquanto o Norte tem a menor (≈ 103). Entre as categorias, "
            "Livros lidera (≈ 187). Os maiores valores individuais são Livros no "
            "Oeste (284,18) e Brinquedos no Oeste (281,17); o menor é Alimentos no "
            "Norte (54,15).\n\n"
            "**Faturamento por canal:** do total de R$ 120 mil, o Site responde por "
            "37,5% e a Loja Física por 26,7%. Somados, Site e Aplicativo (17,5%) "
            "representam 55% do faturamento, o que indica peso maior dos canais "
            "digitais. O Telefone é o menor canal (6,7%)."
        ),
    },
    {
        "titulo": "Distribuições e frequências",
        "graficos": [grafico_distribuicao, grafico_boxplot, grafico_frequencia],
        "analise": (
            "**Idade dos clientes:** a idade média é de 33,6 anos e a mediana, 29. "
            "A moda é 24 anos e as idades vão de 18 a 69. A distribuição é "
            "assimétrica à direita: a maioria é jovem (75% têm até 44 anos) e poucos "
            "clientes mais velhos puxam a média para cima.\n\n"
            "**Salários por departamento:** TI (mediana ≈ R$ 6.614) e Vendas "
            "(≈ R$ 7.130) pagam bem mais que Marketing (≈ R$ 4.191) e RH "
            "(≈ R$ 4.188). TI também tem a maior dispersão. Todos os departamentos "
            "apresentam valores atípicos (outliers) acima do restante do grupo.\n\n"
            "**Tipos de atendimento:** de 300 chamados, Dúvida é o tipo mais comum "
            "(116, ou 38,7%), seguido por Reclamação (73) e Bug (49). Cancelamento "
            "(33) e Elogio (29) são os menos frequentes. Dúvidas, reclamações e bugs "
            "somam mais de 79% dos chamados."
        ),
    },
    {
        "titulo": "Relações entre variáveis e padrões",
        "graficos": [grafico_dispersao, grafico_regressao, grafico_heatmap],
        "analise": (
            "**Altura x Peso:** há correlação positiva forte (r ≈ 0,85): em média, "
            "cada centímetro a mais de altura corresponde a cerca de 0,87 kg a mais "
            "de peso. Os grupos Feminino e Masculino ficam sobrepostos, com médias "
            "muito próximas (≈ 170 cm e 62–63 kg), sem diferença visível entre eles "
            "neste conjunto de dados.\n\n"
            "**Renda x Gasto:** a relação é praticamente linear (r ≈ 0,99). Em média, "
            "o gasto mensal equivale a cerca de 63% da renda, e a reta de regressão "
            "indica um acréscimo de ≈ R$ 0,57 de gasto para cada R$ 1,00 de renda.\n\n"
            "**Movimento de clientes:** o pico ocorre no domingo às 12h (199 clientes) "
            "e o menor movimento, na quinta às 16h (22). Domingo (média ≈ 119) e "
            "sábado (≈ 111) são os dias mais movimentados; quinta é o mais fraco "
            "(≈ 44). O horário das 12h tem a maior média (≈ 90)."
        ),
    },
]

st.title("📊 Atividade de Fixação 07 - Dashboard")
st.caption("Painel interativo de visualização e análise de dados.")

st.info(
    "Este dashboard reúne gráficos de vendas, distribuição de clientes, "
    "relações entre variáveis e movimento de atendimento."
)

metricas = st.columns(3)
metricas[0].metric("Seções", len(LINHAS))
metricas[1].metric("Gráficos", sum(len(item["graficos"]) for item in LINHAS))
metricas[2].metric("Status", "Pronto para executar")



for linha in LINHAS:
    st.subheader(linha["titulo"])
    colunas = st.columns(3)
    for coluna, func in zip(colunas, linha["graficos"]):
        with coluna:
            fig = func()
            st.pyplot(fig)
            plt.close(fig)
    st.markdown("#### 📝 Análise")
    st.markdown(linha["analise"])
    st.divider()
