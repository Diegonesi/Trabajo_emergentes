# Utiliza una imagen base de Ubuntu
FROM ubuntu:latest

# Actualiza el índice de paquetes e instala SQLite
RUN apt-get update && apt-get install -y sqlite3

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el script SQL que inicializa la base de datos (si es necesario)
COPY insert_points.sql .

# Expone el puerto 5432 (puerto predeterminado para SQLite)
EXPOSE 5432

# Comando para ejecutar el servidor SQLite
CMD ["sqlite3", "test.db"]