# ----------------------------------------------------------------------------
# Title:   Generación de datos artificiales para histograma
# Author:  Federico Iza
# ----------------------------------------------------------------------------
import numpy as np

loc = 1.21  # Valor esperado de la distribución normal
scale = 0.12  # Desviación estándar de la distribución normal
size = 300  # Cantidad de datos a generar


if __name__ == '__main__':
	data = np.random.normal(loc, scale, size)
	np.savetxt('data.csv', data)
