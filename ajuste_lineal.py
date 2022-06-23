# ----------------------------------------------------------------------------
# Title:   Ajuste lineal
# Author:  Federico Iza
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from config import config_plots


def linear(x, pendiente, ordenada):
    return ordenada + pendiente*x


def main():
    # Leer datos del directorio errores/
    data = np.loadtxt('datos/errores.csv')
    x, y, y_err = data[:, 0], data[:, 1], data[:, 2]

    # Hacer ajuste
    popt, pcov = curve_fit(linear, x, y, sigma=y_err, absolute_sigma=True)
    perr = np.sqrt(np.diag(pcov))

    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(0, 10)
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_ylim(0, 20)
    plt.errorbar(x, y, y_err, fmt='o', elinewidth=.75, capsize=2, markersize=1)
    plt.plot(x, linear(x, *popt), '--', color='tab:red', lw=1)
    ax.text(.5, 18, '$y(x) = mx+b$', color='tab:red', size=6)
    ax.text(.5, 17, f'$m =$ {round(popt[0], 2)} $\pm$ {round(perr[0], 2)}', color='tab:red', size=6)
    ax.text(.5, 16, f'$b =$ {round(popt[1], 2)} $\pm$ {round(perr[1], 2)}', color='tab:red', size=6)
    fig.savefig('figuras/ajuste_lineal.pdf')
    # plt.show()


if __name__ == '__main__':
    config_plots()
    main()
