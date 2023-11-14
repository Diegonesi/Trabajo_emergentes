import geopandas as gpd
import random
import shapely
import shapely.geometry
import sqlite3
from sqlite3 import Error

def load_shapefile(file_path):
    return gpd.read_file(file_path)

def filter_province(gdf, region_name, province_name):
    gdf = gdf.dropna(subset=['Region'])
    gdf_region = gdf[gdf['Region'].str.contains(region_name)]
    return gdf_region[gdf_region['Provincia'].str.contains(province_name)]

def generate_random_points_within_polygon(polygon, num_points):
    points = []
    min_x, min_y, max_x, max_y = polygon.bounds
    while len(points) < num_points:
        random_point = shapely.geometry.Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if random_point.within(polygon):
            points.append(random_point)
    return points

# Parámetros de configuración
shapefile_path = 'Provincias\Provincias.shp' # Ajusta la ruta al archivo shapefile
db_path = 'valdivia_points.db'        # Ajusta la ruta a la base de datos

# Cargando y filtrando el shapefile
gdf_provincias = load_shapefile(shapefile_path)
provincia_valdivia = filter_province(gdf_provincias, "Los Ríos", "Valdivia")

# Generando puntos aleatorios
valdivia_polygon = provincia_valdivia.iloc[0]['geometry']
random_points = generate_random_points_within_polygon(valdivia_polygon, 100) #cambiar el numero a cuantos puntos se quieran generar.

# Creando el archivo SQL
sql_file_path = 'insert_points.sql'
with open(sql_file_path, 'w') as file:
    file.write('CREATE TABLE IF NOT EXISTS points (id INTEGER PRIMARY KEY, latitude REAL, longitude REAL);\n')
    for idx, point in enumerate(random_points, start=1):
        file.write(f"INSERT INTO points (id, latitude, longitude) VALUES ({idx}, {point.y}, {point.x});\n")

print(f"Archivo SQL generado: {sql_file_path}")

