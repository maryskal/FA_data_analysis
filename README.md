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
En el jupyter notebook se realiza una limpieza de datos sobre el dataset general (puntuacionesFA)

## Generación de subsets
Dado que el dataset general cuenta con muchas columnas que están compuestas por filas, como son directores, guionistas, músicos, fotógrafos, actores, productores y géneros 
si se quieren analizar estos datos en concreto es necesario generar un nuevo dataset por cada una de estas columnas, en el que los componentes de cada una de las columnas 
desglosadas esten representados por una sola fila. Es decir, extender cada lista a lo largo, generando una nueva fila por cada componente de la lista.

![texto cualquiera por si no carga la imagen]
(https://github.com/maryskal/FA_data_analysis/blob/main/image.png?raw=true)
