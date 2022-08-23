# ----------------------------------------------------------------------------
# Title:   Crear histogramas
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from utils.config import config_plots
import pandas as pd


def graficar_ocurrencias():
    # Cargar datos
    df = pd.read_csv('../data/histograma.csv')
    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('Tiempo [s]')
    ax.set_ylabel('Occurencias')
    ax.set_xlim(.8, 1.6)
    ax.set_xticks([.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
    ax.set_ylim(0, 80)
    plt.hist(df['x'], alpha=0.75)
    fig.savefig('../images/histograma_ocurrencias.png')
    # plt.show()


def graficar_pdf():
    # Cargar datos
    df = pd.read_csv('../data/histograma.csv')
    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('Tiempo [s]')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_xlim(.8, 1.6)
    ax.set_xticks([.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
    ax.set_ylim(0, 4.2)
    plt.hist(df['x'], density=True, alpha=0.75)
    fig.savefig('../images/histograma_densidad.png')
    # plt.show()


def graficar_pdf_bineados():
    # Cargar datos
    df = pd.read_csv('../data/histograma.csv')
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
        plt.hist(df['x'], bins=bins, density=True, histtype='step',
                 alpha=0.75, label=bins)
    ax.legend(loc='upper left', framealpha=0)
    fig.savefig('../images/histograma_pdf_bineado.png')
    # plt.show()


if __name__ == '__main__':
    config_plots()
    graficar_ocurrencias()
    graficar_pdf()
    graficar_pdf_bineados()
