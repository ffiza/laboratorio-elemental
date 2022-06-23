# ----------------------------------------------------------------------------
# Title:   Crear histogramas
# Author:  Federico Iza
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from config import config_plots


def graficar_ocurrencias():
    # Cargar datos
    data = np.loadtxt('datos/histograma.csv')
    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('Tiempo [s]')
    ax.set_ylabel('Occurencias')
    ax.set_xlim(.8, 1.6)
    ax.set_xticks([.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
    ax.set_ylim(0, 80)
    plt.hist(data, alpha=0.75)
    fig.savefig('figuras/histograma_ocurrencias.png')
    # plt.show()


def graficar_pdf():
    # Cargar datos
    data = np.loadtxt('datos/histograma.csv')
    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('Tiempo [s]')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_xlim(.8, 1.6)
    ax.set_xticks([.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
    ax.set_ylim(0, 4.2)
    plt.hist(data, density=True, alpha=0.75)
    fig.savefig('figuras/histograma_densidad.png')
    # plt.show()


def graficar_pdf_bineados():
    # Cargar datos
    data = np.loadtxt('datos/histograma.csv')
    # Definir tres bineados
    binnings = [10, 15, 20]  # Número de bines
    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('Tiempo [s]')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_xlim(.8, 1.6)
    ax.set_xticks([.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
    ax.set_ylim(0, 4.2)
    for bins in binnings:
        plt.hist(data, bins=bins, density=True, histtype='step', alpha=0.75,
                 label=bins)
    ax.legend(loc='upper left', framealpha=0)
    fig.savefig('figuras/histograma_pdf_bineado.png')
    # plt.show()


if __name__ == '__main__':
    config_plots()
    graficar_ocurrencias()
    graficar_pdf()
    graficar_pdf_bineados()
