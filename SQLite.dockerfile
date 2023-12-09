# Usa una imagen base de SQLite
FROM alpine:latest

# Establece el directorio de trabajo
WORKDIR /app

# Instala SQLite
RUN apk --no-cache add sqlite

# Copia el archivo SQL a la imagen
COPY insert_points.sql /app/

# Inicializa la base de datos con el archivo SQL
RUN sqlite3 mydatabase.db < insert_points.sql

# Comando por defecto al ejecutar el contenedor
CMD ["sqlite3", "mydatabase.db"]