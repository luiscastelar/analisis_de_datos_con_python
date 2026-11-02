# Imagen base ligera de Python
FROM python:3.11-slim

# Lo público
EXPOSE 8000
VOLUME app

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Comando para ejecutar FastAPI usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

