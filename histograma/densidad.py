# ----------------------------------------------------------------------------
# Title:   Crear histograma con densidad de probabilidad
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

    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('Tiempo [s]')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_xlim(.8, 1.5)
    ax.set_xticks([.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
    ax.set_ylim(0, 4)
    plt.hist(data, density=True, alpha=0.7)
    # plt.show()
    fig.savefig('densidad.pdf')


if __name__ == '__main__':
    config_plots()
    main()
