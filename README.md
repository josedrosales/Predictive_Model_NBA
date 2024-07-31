# NBA puntos por jugador - 4Geeks Final Project

## Introducción 

Este repositorio contiene el proyecto final del Bootcamp de 4Geeks, en esta instancia decidimos utilizar datos de la NBA para entrenar un modelo de regresión el cual nos permita predecir la cantidad de puntos que un jugador va a anotar en un partido dado un conjunto de estadísticas promedio de juegos anteriores.

Nuestro objetivo es que el usuario elija un jugador e introduzca los promedios de: 
- Puntos
- Minutos
- Tiros de campo intentados
- Faltas recibidas
  
Y luego la aplicación le devuelva la cantidad de puntos que el jugador convertirá de acuerdo a los valores introducidos.

## Dataset

Decidimos obtener los datos con los cuales estaremos trabajando desde la [NBA_API](https://github.com/swar/nba_api), utilizando distintos endpoints proporcionados por la misma para la obtención de los datos desados.

El conjunto de datos consta de las estadísticas personales de cada jugador y cada partido disputados en las temporadas 2020-21, 2021-22, 2022-23.


### Permanencia de datos

Se creó una instancia SQL, utilizando la librería ``sqlite3``, y se volcaron los datos del dataset dentro de la base de datos 'NBA.db' y dentro de la tabla `ESTADISTICAS`.
Realizamos algunas consultas sobre la DB para corroborar que todo estuviese correcto.



### Análisis descriptivo y análisis exploratorio de datos

Se crearon nuevas columnas a partir de las ya existentes, mediante una función la cual calcula el promedio de los 5 partidos anteriores para una estadística especificada.<br>
No fue necesario hacer ningún tratamiento a los valores nulos ya que no se encontró ninguno.<br>
Se observaron las relaciones lineales importantes y las irrelevantes, a partir de las mismas se eliminaron variables que consideramos irrelevantes para nuestro caso.<br>
Todo esto se puede ver en el archivo `src/Preprocesamiento.ipynb`
<br>
<br>
<br>
Luego de analizado y modificado el dataset, quedan 20 columnas y 74987 filas, conteniendo los datos de 784 jugadores, 30 equipos y 3540 partidos.

El dataset completo se puede encontrar en `data/raw/data_complete_raw.csv`, mientras que el dataset modificado se encuentra en `data/processed/data_clean.csv`

## Modelo

Se realizó una evaluación con los modelos base `Lineal, Lasso, Ridge, Decision Tree, Random Forest, Boosting y K-neighbors` con los parámetros por default. <br>
A partir de la evaluación anterior se tomaron los 3 modelos con el mejor rendimiento, evaluados mediante el R^2 y RMSE. <br>
Luego realizamos un proceso de optimización de los hiperparámetros, tanto con el método de RandomSearch como el de GridSearch. <br>
Comparando nuevamente los resultados, concluimos que el Random Forest fue el que nos arrojó los mejores resultados, por lo tanto fue el modelo seleccionado.

## Aplicación

A partir del modelo generado se utilizan las 5 variables predictoras `Jugador, Minutos promedio, Intentos de tiros de campo, Puntos promedio y Faltas recibidas` y la variable a predecir `Puntos`. <br>
La variable del `Jugador` la mostramos en la aplicación como una lista desplegable mientras que el resto de variables predictoras se muestran como un slider. <br>

## Ejecutar la aplicación
Para ejecutar la aplicación se debe ejecutar el siguiente comando:
```bash
streamlit run src/app.py
```
De igual forma puede usar el siguiente enlace: https://predictive-model-nba.onrender.com

## Autores
[José Rosales](https://github.com/josedrosales)<br>
[Sebastián Centurión](https://github.com/sebacent)
