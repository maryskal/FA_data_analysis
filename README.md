# Analisis de las películas favoritas de un usuario
Inicialmente contamos con un dataset (puntuacionesFA) que recoge todas las peliculas votadas por un usuario, con las siguientes columnas:

- titulo
- año          
- duracion       
- pais           
- directores     
- guionistas     
- musicos        
- fotografos     
- actores        
- productores    
- generos        
- nota           
- votos          
- votacion 

## Limpieza de datos
En el jupyter notebook (1_data_cleaning.ipynb) se realiza una limpieza de datos sobre el dataset general (puntuacionesFA)

## Generación de subsets
Dado que el dataset general cuenta con muchas columnas que están compuestas por filas, como son directores, guionistas, músicos, fotógrafos, actores, productores y géneros 
si se quieren analizar estos datos en concreto es necesario generar un nuevo dataset por cada una de estas columnas, en el que los componentes de cada una de las columnas 
desglosadas esten representados por una sola fila. Es decir, extender cada lista a lo largo, generando una nueva fila por cada componente de la lista.

![Error de imagen](https://github.com/maryskal/FA_data_analysis/blob/main/image.png?raw=true)

Para generar los subsets tenemos un ejecutable en el que se introduce la columna de la cual se quiere generar el subset y este se genera y se guarda en la carpeta principal

´python 2_extract_subsets.py -c directores´

## Análisis de datos
Para el análisis de datos hemos utilizado R.Markdown para generar un informe HTML en el cual hemos analizado las características generales del dataset original (puntuacionesFA) y luego hemos analizado las características de los directores, guionistas y géneros.
