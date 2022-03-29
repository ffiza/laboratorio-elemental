# ----------------------------------------------------------------------------
# Title:   Crear histograma de densidad con distinto bineado
# Author:  Federico Iza
# ----------------------------------------------------------------------------
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Agregar path para usar config.py
from config import config_plots


def main():
    # Cargar datos
    data = np.loadtxt('data.csv')

    # Definir tres bineados
    binnings = [10, 15, 20]  # Número de bines

    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('Tiempo [s]')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_xlim(.8, 1.5)
    ax.set_xticks([.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
    ax.set_ylim(0, 4)
    for bins in binnings:
        plt.hist(data, bins=bins, density=True, histtype='step', alpha=0.5, label=bins)
    ax.legend(loc='upper left', framealpha=0)
    plt.show()
    fig.savefig('bineado.pdf')


if __name__ == '__main__':
    config_plots()
    main()
