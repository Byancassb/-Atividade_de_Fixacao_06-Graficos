import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ARQUIVO_DADOS = "dados/dados_linhas.csv"
ARQUIVO_SAIDA = "grafico_linhas.png"


def gerar_grafico_linhas():
    dados = pd.read_csv(ARQUIVO_DADOS)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="data", y="vendas", hue="loja", data=dados, ax=ax)
    ax.set_title("Evolução de Vendas por Loja")
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    fig.savefig(ARQUIVO_SAIDA)
    plt.show()


if __name__ == "__main__":
    gerar_grafico_linhas()
