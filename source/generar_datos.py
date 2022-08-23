# Title:   Generación de datos artificiales

import numpy as np


def gen_datos_errores(xmin: float = 0, xmax: float = 10, size: int = 20,
                      slope: float = 1.5, intercept: float = 1) -> None:
    """
    Genera datos artificiales a partir de una función lineal y ruido normal.

    :param xmin: Valor mínimo del rango de datos a generar.
    :param xmax: Valor máximo del rango de datos a generar.
    :param size: Cantidad de datos a generar.
    :param slope: Pendiente de la función lineal base.
    :param intercept: Ordenada de la función lineal base.
    """

    # Generar datos
    x = np.sort(np.random.uniform(xmin, xmax, size))
    noise = np.random.normal(0, 1, size)
    y = intercept + slope * x + noise
    y_err = np.linspace(.5, 1.5, size)
    data = np.vstack((x, y, y_err)).T

    # Guardar datos
    np.savetxt(fname='../data/errores.csv', X=data, header='x y y_err')


def gen_datos_histograma(loc: float = 1.21, scale: float = 0.12,
                         size: int = 300) -> None:
    """
    Genera datos artificiales tomados de una distribución normal.

    :param loc: Valor esperado de la distribución normal.
    :param scale: Desviación estándard de la distribución normal.
    :param size: Cantidad de datos a generar.
    """

    # Generar datos
    data = np.random.normal(loc, scale, size)

    # Guardar datos
    np.savetxt(fname='../data/histograma.csv', X=data, header='x')


if __name__ == '__main__':
    gen_datos_errores()
    gen_datos_histograma()
