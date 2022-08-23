# ----------------------------------------------------------------------------
# Title:   Crear scatter plot
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from utils.config import config_plots
import pandas as pd


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
    plt.scatter(df['x'], df['y'], s=15, linewidths=.5, edgecolors='white')
    # plt.show()
    fig.savefig('../images/scatter.png')


if __name__ == '__main__':
    config_plots()
    main()
