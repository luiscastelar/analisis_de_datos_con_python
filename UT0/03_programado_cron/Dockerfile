FROM python:3.11-slim

# 1. Instalar el paquete cron y tzdata para la zona horaria
RUN apt-get update && apt-get install -y --no-install-recommends \
    cron \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# 2. Configurar la zona horaria a nivel de sistema operativo
ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 3. Directorio de trabajo
WORKDIR /app

# 4. Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar los scripts de Python
COPY *.py ./

# 6. Copiar el archivo crontab al directorio del sistema
COPY crontab /etc/cron.d/mi-cron

# 7. Dar permisos correctos a la tarea y registrarla en cron
RUN chmod 0644 /etc/cron.d/mi-cron && crontab /etc/cron.d/mi-cron

# 8. Arrancar el demonio cron en primer plano (-f)
CMD ["cron", "-f"]
