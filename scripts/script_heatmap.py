import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ARQUIVO_DADOS = "dados/dados_heatmap.csv"
ARQUIVO_SAIDA = "grafico_heatmap.png"


def gerar_heatmap():
    dados = pd.read_csv(ARQUIVO_DADOS)


    matriz = dados.pivot(
        index="dia_semana", columns="horario", values="movimento_clientes"
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(matriz, annot=True, fmt="g", cmap="YlGnBu", ax=ax)
    ax.set_title("Heatmap: Movimento de Clientes por Dia e Horário")

    fig.tight_layout()
    fig.savefig(ARQUIVO_SAIDA)
    plt.show()


if __name__ == "__main__":
    gerar_heatmap()
