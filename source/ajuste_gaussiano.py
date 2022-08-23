# ----------------------------------------------------------------------------
# Title:   Ajuste gaussiano
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
from utils.config import config_plots
import sys


def gaussian(x, mu, sigma):
    amplitude = 1 / sigma / np.sqrt(2*np.pi)
    exponent = - 0.5 * (x - mu)**2 / sigma**2
    return amplitude * np.exp(exponent)


def main():
    # Leer datos
    df = pd.read_csv('../data/histograma.csv')

    # Construir histograma
    hist, bin_edges = np.histogram(df['x'], density=True)
    bin_centers = bin_edges[1:] - np.diff(bin_edges)[0]/2

    # Hacer ajuste
    popt, pcov = curve_fit(gaussian, bin_centers, hist)
    perr = np.sqrt(np.diag(pcov))

    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('Tiempo [s]')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_xlim(0.8, 1.6)
    ax.set_xticks([.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
    ax.set_ylim(0, 4.2)
    plt.hist(df['x'], density=True, alpha=0.75)
    x = np.linspace(0.8, 1.6, 100)
    plt.plot(x, gaussian(x, *popt), '--', color='tab:red', lw=1)

    fig.savefig('../images/ajuste_gaussiano.png')
    # plt.show()

    # Print fit results
    sys.stdout.write('FIT RESULTS\n')
    sys.stdout.write(f'Mu: {round(popt[0], 3)} +- {round(perr[0], 3)}\n')
    sys.stdout.write(f'Sigma: {round(popt[1], 3)} +- {round(perr[1], 3)}\n')


if __name__ == '__main__':
    config_plots()
    main()
