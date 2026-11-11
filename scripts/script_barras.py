import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ARQUIVO_DADOS = "dados/dados_barras.csv"
ARQUIVO_SAIDA = "grafico_barras.png"


def gerar_grafico_barras():
    dados = pd.read_csv(ARQUIVO_DADOS)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="categoria", y="vendas_medias", hue="regiao", data=dados, ax=ax)
    ax.set_title("Vendas Médias por Categoria e Região")

    fig.tight_layout()
    fig.savefig(ARQUIVO_SAIDA)
    plt.show()


if __name__ == "__main__":
    gerar_grafico_barras()
