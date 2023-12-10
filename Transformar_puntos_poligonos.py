#Instalar biblioteca: pip install pyproj
from pyproj import CRS, Transformer
import sqlite3
import subprocess

# Nombre o ID del contenedor
nombre_contenedor = 'sqlite'

# Inicializa el contenedor
comando = f"sudo docker build -f SQLite.dockerfile -t {nombre_contenedor} ./"
subprocess.run(comando, shell=True)
comando = f"sudo docker run -d --name {nombre_contenedor} {nombre_contenedor}"
subprocess.run(comando, shell=True)

# Se recupera la base de datos al local de manera temporal
ruta_contenedor = '/app/mydatabase.db'
comando = f"sudo docker cp {nombre_contenedor}:{ruta_contenedor} ."
subprocess.run(comando, shell=True)

# Conectar a la base de datos SQLite dentro del contenedor
conn = sqlite3.connect(f'mydatabase.db')

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Ejecutar una consulta SELECT
cursor.execute("SELECT * FROM points")

# Obtener todos los resultados
resultados = cursor.fetchall()

# Definir los sistemas de coordenadas de entrada y salida
entrada = CRS.from_epsg(3857)  # EPSG:4326 es el sistema de coordenadas de latitud y longitud
salida = CRS.from_epsg(32719)  # Formato solicitado

# Crear un transformador
transformador = Transformer.from_crs(entrada, salida)

# Convertir las coordenadas (fila[2]: longitud, fila[1]: latitud)
coordenadas_convertidas = [(fila[0],) + transformador.transform(fila[2], fila[1]) for fila in resultados]

# Cerrar la conexión y borrar la base de datos recuperada temporalmente
conn.close()
comando = f"sudo rm mydatabase.db"
subprocess.run(comando, shell=True)

# Actualizar el archivo SQL
sql_file_path = 'insert_points.sql'
with open(sql_file_path, 'a') as file:
    file.write('\nCREATE TABLE IF NOT EXISTS points_EPSG32719 (id INTEGER PRIMARY KEY, x REAL, y REAL);\n')
    for id, points in enumerate(coordenadas_convertidas, start=1):
        #print("points", points)
        file.write(f"INSERT INTO points_EPSG32719 (id, x, y) VALUES ({id}, {points[1]}, {points[2]});\n")


# Se elimina y vuelve a crear el contenedor para actualizar la base de datos
comando = f"sudo docker stop {nombre_contenedor} && sudo docker rm {nombre_contenedor}"
subprocess.run(comando, shell=True) 
comando = f"sudo docker build -f SQLite.dockerfile -t {nombre_contenedor} ./"
subprocess.run(comando, shell=True) 
