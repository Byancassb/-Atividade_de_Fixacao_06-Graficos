import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ARQUIVO_DADOS = "dados/dados_frequencia.csv"
ARQUIVO_SAIDA = "grafico_frequencia.png"


def gerar_grafico_frequencia():
    dados = pd.read_csv(ARQUIVO_DADOS)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x="tipo_atendimento", data=dados, ax=ax)
    ax.set_title("Frequência por Tipo de Atendimento")

    fig.tight_layout()
    fig.savefig(ARQUIVO_SAIDA)
    plt.show()


if __name__ == "__main__":
    gerar_grafico_frequencia()
