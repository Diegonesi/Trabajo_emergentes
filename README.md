Se busco el archivo de poligonos de Valdivia en la biblioteca nacional (https://www.bcn.cl/siit/mapas_vectoriales)

Se creo un codigo para poder generar coordenadas aleatorias dentro de las zonas urbanas de valdivia y comunas pobladas vecinas pip install geopandas Se creo un Dockerfile con una base de datos en SQLite, para poder ingresar los resultados de los datos generados

Podemos los shadesfiles online en este archivo: https://products.aspose.app/gis/viewer/shp

Para correr el Docker en windows se utiliza los siguientes comandos 
docker build -f .\SQLite.dockerfile -t sqlite ./ 
docker run -it -p 8080:80 --name sqlite sqlite 
La tabla de datos es "mydatabase.db"

Una vez se ejecuta el codigo de genera_puntos, hay que ejecutar el archivo transformar_puntos, el cual cambiara el insert_points.sql el cual entregara una nueva base de datos con los datos en el formato EPSG:32719