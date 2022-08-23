# ----------------------------------------------------------------------------
# Title:   Crear gráfico con barras de error
# ----------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
from utils.config import config_plots


def main():
    # Cargar datos
    df = pd.read_csv('../data/errores.csv')
    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(0, 10)
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_ylim(0, 20)
    plt.errorbar(df['x'], df['y'], df['y_err'], fmt='o', elinewidth=.75,
                 capsize=2, markersize=1)
    fig.savefig('../images/errores.png')
    # plt.show()


if __name__ == '__main__':
    config_plots()
    main()
