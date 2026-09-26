# Imagen base oficial de Python (versión slim para reducir tamaño)
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia e instala las dependencias primero para aprovechar el caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente al contenedor
COPY hola_mundo.py .

# Comando por defecto que se ejecuta al iniciar el contenedor
CMD ["python", "hola_mundo.py"]
