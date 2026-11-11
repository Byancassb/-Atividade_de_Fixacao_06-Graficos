import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ARQUIVO_DADOS = "dados/dados_dispersao.csv"
ARQUIVO_SAIDA = "grafico_dispersao.png"


def gerar_grafico_dispersao():
    dados = pd.read_csv(ARQUIVO_DADOS)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x="altura_cm", y="peso_kg", hue="sexo", data=dados, ax=ax)
    ax.set_title("Dispersão: Altura vs Peso por Sexo")

    fig.tight_layout()
    fig.savefig(ARQUIVO_SAIDA)
    plt.show()


if __name__ == "__main__":
    gerar_grafico_dispersao()
