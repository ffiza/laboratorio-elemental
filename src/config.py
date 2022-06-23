# ----------------------------------------------------------------------------
# Title:   Script para configurar los gráficos
# Author:  Federico Iza
# ----------------------------------------------------------------------------
import matplotlib.pyplot as plt
from distutils.spawn import find_executable


def config_plots():
    params = {'figure.dpi': 500,
              'figure.figsize': [3, 2.5],
              'font.size': 8,
              'font.family': 'serif',
              'axes.labelsize': 10,
              'xtick.top': 'on',
              'xtick.minor.bottom': 'on',
              'xtick.minor.top': 'on',
              'xtick.direction': 'in',
              'ytick.right': 'on',
              'ytick.minor.left': 'on',
              'ytick.minor.right': 'on',
              'ytick.direction': 'in',
              'savefig.dpi': 300,
              'savefig.bbox': 'tight',
              'savefig.pad_inches': .02,
              'axes.axisbelow': True,
              'axes.grid': True,
              'grid.linestyle': '--',
              'grid.linewidth': .5}
    # Si LaTeX está instalado, usar sus fuentes
    if find_executable('latex'):
        params['text.usetex'] = True
    plt.rcParams.update(params)
