import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ARQUIVO_DADOS = "dados/dados_distribuicao.csv"
ARQUIVO_SAIDA = "grafico_distribuicao.png"


def gerar_grafico_distribuicao():
    dados = pd.read_csv(ARQUIVO_DADOS)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(x="idade", data=dados, kde=True, ax=ax)
    ax.set_title("Distribuição de Idade dos Clientes")

    fig.tight_layout()
    fig.savefig(ARQUIVO_SAIDA)
    plt.show()


if __name__ == "__main__":
    gerar_grafico_distribuicao()
