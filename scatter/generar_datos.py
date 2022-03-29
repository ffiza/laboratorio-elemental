# ----------------------------------------------------------------------------
# Title:   Generación de datos artificiales para scatter
# Author:  Federico Iza
# ----------------------------------------------------------------------------
import numpy as np

x_min, x_max = 0, 10  # Valores extremos del eje x
size = 20  # Cantidad de datos a generar
slope = 1.5   # Pendiente
intercept = 1  # Ordenada al origen


if __name__ == '__main__':
	# Generar datos
	x = np.sort(np.random.uniform(0, 10, size))
	noise = np.random.normal(0, 1, size)
	y = intercept + slope * x + noise

	data = np.vstack((x, y)).T
	np.savetxt('data.csv', data, header='x y')
