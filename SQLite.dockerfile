# Usa la imagen oficial de SQLite desde Docker Hub
FROM sqlite:latest

# Copia tu base de datos SQLite al contenedor
COPY mi_base_de_datos.db /ruta/del/contenedor/mi_base_de_datos.db

# Opcional: Define el directorio de trabajo
WORKDIR /ruta/del/contenedor/

# Opcional: Cambiar al puerto a utilizar, por defecto esta:
# EXPOSE 5432

# Opcional: Define el comando por defecto para ejecutar cuando se inicia el contenedor
# CMD ["sqlite3", "valdivia_points.db"]
