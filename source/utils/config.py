# Title:   Script para configurar los gráficos

import matplotlib.pyplot as plt
from distutils.spawn import find_executable

DPI = 500
FIGSIZE = (3, 2.5)
FONTSIZE = 8
LABELSIZE = 10
PAD_INCHES = 0.02
GRID_LINEWIDTH = 0.5


def config_plots() -> None:
    """
    Función que configura la apariencia de los gráficos haciendo uso de las
    variables definidas en config.py.
    """
    params = {'figure.dpi': DPI,
              'figure.figsize': FIGSIZE,
              'font.size': FONTSIZE,
              'font.family': 'serif',
              'axes.labelsize': LABELSIZE,
              'xtick.top': 'on',
              'xtick.minor.bottom': 'on',
              'xtick.minor.top': 'on',
              'xtick.direction': 'in',
              'ytick.right': 'on',
              'ytick.minor.left': 'on',
              'ytick.minor.right': 'on',
              'ytick.direction': 'in',
              'savefig.dpi': DPI,
              'savefig.bbox': 'tight',
              'savefig.pad_inches': PAD_INCHES,
              'axes.axisbelow': True,
              'axes.grid': True,
              'grid.linestyle': '--',
              'grid.linewidth': GRID_LINEWIDTH}
    # Si LaTeX está instalado, usar sus fuentes
    if find_executable('latex'):
        params['text.usetex'] = True
    plt.rcParams.update(params)
