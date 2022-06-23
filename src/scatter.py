# ----------------------------------------------------------------------------
# Title:   Crear scatter plot
# Author:  Federico Iza
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from config import config_plots


def main():
    # Cargar datos
    data = np.loadtxt('datos/errores.csv')
    x, y = data[:, 0], data[:, 1]

    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(0, 10)
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_ylim(0, 20)
    plt.scatter(x, y, s=15, linewidths=.5, edgecolors='white')
    # plt.show()
    fig.savefig('figuras/scatter.png')


if __name__ == '__main__':
    config_plots()
    main()
