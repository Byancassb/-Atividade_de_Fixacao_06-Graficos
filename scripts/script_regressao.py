import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ARQUIVO_DADOS = "dados/dados_regressao.csv"
ARQUIVO_SAIDA = "grafico_regressao.png"


def gerar_grafico_regressao():
    dados = pd.read_csv(ARQUIVO_DADOS)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.regplot(x="renda_mensal", y="gasto_mensal", data=dados, ax=ax)
    ax.set_title("Regressão: Renda Mensal vs Gasto Mensal")

    fig.tight_layout()
    fig.savefig(ARQUIVO_SAIDA)
    plt.show()


if __name__ == "__main__":
    gerar_grafico_regressao()
