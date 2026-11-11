import matplotlib.pyplot as plt
import pandas as pd

ARQUIVO_DADOS = "dados/dados_pizza.csv"
ARQUIVO_SAIDA = "grafico_pizza.png"


def gerar_grafico_pizza():
    dados = pd.read_csv(ARQUIVO_DADOS)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(
        dados["faturamento"],
        labels=dados["canal_venda"],
        autopct="%1.1f%%",
        startangle=140,
    )
    ax.set_title("Faturamento por Canal de Venda")

    fig.tight_layout()
    fig.savefig(ARQUIVO_SAIDA)
    plt.show()


if __name__ == "__main__":
    gerar_grafico_pizza()
