# ----------------------------------------------------------------------------
# Title:   Ajuste lineal
# Author:  Federico Iza
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from utils.config import config_plots


def linear(x, pendiente, ordenada):
    return ordenada + pendiente*x


def main():
    # Leer datos
    df = pd.read_csv('../data/errores.csv')

    # Hacer ajuste
    popt, pcov = curve_fit(linear, df['x'], df['y'], sigma=df['y_err'], absolute_sigma=True)
    perr = np.sqrt(np.diag(pcov))

    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(0, 10)
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_ylim(0, 20)
    plt.errorbar(df['x'], df['y'], df['y_err'], fmt='o', elinewidth=.75, capsize=2, markersize=1)
    plt.plot(df['x'], linear(df['x'], *popt), '--', color='tab:red', lw=1)
    ax.text(.5, 18, '$y(x) = mx+b$', color='tab:red', size=6)

    slope_str = f'$m =$ {round(popt[0], 2)} ' + rf'$\pm$ {round(perr[0], 2)}'
    ax.text(.5, 17, slope_str, color='tab:red', size=6)
    inter_str = f'$b =$ {round(popt[1], 2)} ' + rf'$\pm$ {round(perr[1], 2)}'
    ax.text(.5, 16, inter_str, color='tab:red', size=6)

    fig.savefig('../images/ajuste_lineal.png')
    # plt.show()


if __name__ == '__main__':
    config_plots()
    main()
