# Trabajo_emergentes
Se busco el archivo de poligonos de Valdivia en la biblioteca nacional (https://www.bcn.cl/siit/mapas_vectoriales)

Se creo un codigo para poder generar coordenadas aleatorias dentro de las zonas urbanas de valdivia y comunas pobladas vecinas
pip install geopandas
Se creo un Dockerfile con una base de datos en SQLite, para poder ingresar los resultados de los datos generados

Para correr el Docker en windows se utiliza los siguientes comandos
docker build -f .\SQLite.dockerfile -t sqlite ./
docker run -it -p 8080:80 sqlite 