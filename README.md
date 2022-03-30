# Laboratorio 1

Colección de scripts de Python para generar figuras útiles en la materia Laboratorio 1 de FCEyN.

## Descripción

## ```histograma/```

- ```histograma/ocurrencias.py```: Genera un histograma donde el eje vertical tiene la cantidad de ocurrencias en cada bin.
- ```histograma/densidad.py```: Genera un histograma donde el eje vertical tiene la densidad de probabilidad. Esto se logra usando ```density=True``` en ```plt.hist```.
- ```histograma/bineado.py```: Genera la densidad de probabilidad para tres bineados distintos.
- ```histograma/generar_datos.py```: Script que genera datos artificiales para ser usados en los histogramas.
- ```histograma/data.csv```: Contiene los datos generados por ```generar_datos.py```.

## ```scatter/```

- ```scatter/scatter.py```: Genera un gráfico tipo _scatter_.
- ```scatter/generar_datos.py```: Script que genera datos artificiales para ser usados en los gráficos.
- ```scatter/data.csv```: Contiene los datos generados por ```generar_datos.py```.

## ```errores/```

- ```errores/errores.py```: Genera un gráfico de puntos con barras de error en el eje vertical.
- ```errores/generar_datos.py```: Script que genera datos artificiales para ser usados en los gráficos.
- ```errores/data.csv```: Contiene los datos generados por ```generar_datos.py```.

## ```ajustes/```

- ```ajustes/lineal.py```: Genera un gráfico con los datos en ```errores/data.csv``` y hace un ajuste lineal sobre los mismos.