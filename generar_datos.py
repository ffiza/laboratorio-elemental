# ----------------------------------------------------------------------------
# Title:   Generación de datos artificiales
# Author:  Federico Iza
# ----------------------------------------------------------------------------
import numpy as np


def gen_datos_errores():
    xmin, xmax = 0, 10  # Valores extremos del eje x
    size = 20  # Cantidad de datos a generar
    slope = 1.5   # Pendiente
    intercept = 1  # Ordenada al origen
    # Generar datos
    x = np.sort(np.random.uniform(xmin, xmax, size))
    noise = np.random.normal(0, 1, size)
    y = intercept + slope * x + noise
    y_err = np.linspace(.5, 1.5, size)
    data = np.vstack((x, y, y_err)).T
    np.savetxt(fname='datos/errores.csv', X=data, header='x y y_err')


def gen_datos_histograma():
    loc = 1.21  # Valor esperado de la distribución normal
    scale = 0.12  # Desviación estándar de la distribución normal
    size = 300  # Cantidad de datos a generar
    # Generar datos
    data = np.random.normal(loc, scale, size)
    np.savetxt(fname='datos/histograma.csv', X=data, header='x')


if __name__ == '__main__':
    gen_datos_errores()
    gen_datos_histograma()
