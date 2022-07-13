# Laboratorio 1

Colección de scripts de Python para generar figuras útiles en la materia Laboratorio 1 de FCEyN.

## Descripción

- ```source/```
  - ```ajuste_gaussiano.py```: Grafica un histograma con los datos en ```data/histograma.csv``` y hace un ajuste gaussiano.
  - ```ajuste_lineal.py```: Grafica los datos en ```data/errores.csv``` y hace un ajuste lineal sobre los mismos.
  - ```errores.py```: Grafica los datos en ```data/errores.csv``` como puntos con barras de error en el eje vertical.
  - ```generar_datos.py```: Genera datos artificiales para ser usados en los gráficos.
  - ```histograma.py```: Genera tres histogramas (ocurrencias, densidad de probabilidad y densidad de probabilidad con distinto bineado) a partir de los datos ```data/histograma.csv```.
  - ```scatter.py```: Genera un gráfico tipo _scatter_ (sin barras de error) de los datos en ```data/errores.csv```.
  - ```utils/```
    - ```config.py```: Contiene una función que configura el aspecto de los gráficos.