import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
ALUNO = {
    "Nome": "Rafael Vieira Gozaga",
    "Número da chamada": "34",
    "Turma": "3D2",
}

st.set_page_config(
    page_title="Página de Gráficos",
    page_icon="😂",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.subheader("Barra lateral")
st.sidebar.markdown(f"Nome: {ALUNO['Nome']}")
st.sidebar.markdown(f"Turma: {ALUNO['Turma']}")
st.sidebar.markdown(f"N° de chamada: {ALUNO['Número da chamada']}")

st.title("Gráficos")
st.caption("Está pagina contem gráficos da att6")

st.divider()

st.write("Conteúdo abaixo da linha")
col1, col2, col3= st.columns([1,1,1])
with col1:
    st.subheader("Gráfico de barras")
    st.caption("Compara a média de vendas entre as categorias de produtos, separadas por região (Norte, Sul, Leste e Oeste). Cada cor representa uma região, o que permite ver qual categoria vende mais e em qual região. A região Oeste tem a maior média geral e a Norte a menor.")
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
    st.pyplot(fig)

with col2:
    st.subheader("Gráfico de dispersão")
    st.caption("Cada ponto é uma pessoa, relacionando altura (eixo X) e peso (eixo Y), com cores por sexo. A linha cinza é a tendência: quanto maior a altura, maior o peso (correlação positiva forte, cerca de 0,85).")
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
    st.pyplot(fig)

with col3:
    st.subheader("Gráfico de boxplot")
    st.caption("Mostra a distribuição dos salários em cada departamento: a linha central da caixa é a mediana, a caixa vai do 1º ao 3º quartil e os pontos isolados são outliers. Vendas e TI têm as maiores medianas; Marketing e RH têm salários mais baixos e parecidos.")
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
    st.pyplot(fig)


st.divider()
st.write("Conteúdo abaixo da linha")
col1, col2, col3= st.columns([1,1,1])
with col1: 
    st.subheader("Gráfico de Linhas")
    st.caption("Mostra a evolução diária das vendas de janeiro a março de 2026. A linha permite identificar tendências, picos e quedas ao longo do tempo. As vendas oscilam entre cerca de 93 e 260, com média perto de 174, e terminam o período em alta.")
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
    st.pyplot(fig)

with col2:
    st.subheader("Gráfico de pizza")
    st.caption("Gráfico de rosca que mostra a participação de cada canal de venda no faturamento total. O Site lidera (37,5%), seguido da Loja Física (26,7%) e do Aplicativo (17,5%); Parceiros (11,7%) e Telefone (6,7%) contribuem menos.")
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
    st.pyplot(fig)

with col3:
    st.subheader("Gráfico de regressão")
    st.caption("Relaciona a renda mensal (eixo X) ao gasto mensal (eixo Y), com uma linha de regressão. A linha sobe e os pontos ficam muito próximos dela (correlação de cerca de 0,99): quanto maior a renda, maior o gasto.")
    df_regressao = pd.read_csv("dados_regressao.csv")

    fig, ax = plt.subplots(figsize=(8, 4))

    sns.scatterplot(
        data=df_regressao,
        x="renda_mensal",
        y="gasto_mensal",
        alpha=0.8,
        ax=ax
    )

    sns.regplot(
        data=df_regressao,
        x="renda_mensal",
        y="gasto_mensal",
        scatter=False,
        color="gray",
        ax=ax
    )

    ax.set_title("Relação entre Renda e Gasto Mensal", fontweight="bold")
    ax.set_xlabel("Renda Mensal (R$)")
    ax.set_ylabel("Gasto Mensal (R$)")

    plt.tight_layout()
    st.pyplot(fig)

st.divider()
st.write("Conteúdo abaixo da linha")
col1, col2, col3= st.columns([1,1,1])
with col1: 
    st.subheader("Gráfico de distribuição")
    st.caption("Histograma com curva KDE da idade dos 200 clientes. As barras mostram quantos clientes há em cada faixa etária e a curva suaviza o formato da distribuição. A idade média é de cerca de 34 anos, com concentração de clientes mais jovens (mediana de 29).")
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
    st.pyplot(fig)

with col2:
    st.subheader("Gráfico de frequência")
    st.caption("Conta quantos chamados de atendimento existem de cada tipo. Dúvidas são o tipo mais frequente (116 chamados), seguidas por Reclamações (73), Bugs (49), Cancelamentos (33) e Elogios (29).")
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
    st.pyplot(fig)

with col3:
    st.subheader("Gráfico de heatmap")
    st.caption("Mapa de calor do movimento de clientes por dia da semana e horário. Cores mais quentes indicam mais clientes e cores frias, menos. O pico é no domingo às 12:00 (199 clientes) e o menor movimento é na quinta às 16:00 (22 clientes).")
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
    st.pyplot(fig)