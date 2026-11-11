import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ARQUIVO_DADOS = "dados/dados_boxplot.csv"
ARQUIVO_SAIDA = "grafico_boxplot.png"


def gerar_boxplot():
    dados = pd.read_csv(ARQUIVO_DADOS)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="departamento", y="salario", data=dados, ax=ax)
    ax.set_title("Distribuição de Salários por Departamento")

    fig.tight_layout()
    fig.savefig(ARQUIVO_SAIDA)
    plt.show()


if __name__ == "__main__":
    gerar_boxplot()
