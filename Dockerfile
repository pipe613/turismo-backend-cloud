# Usamos una imagen oficial y ligera de Python
FROM python:3.12-slim

# Configuraciones para que Python funcione mejor en contenedores
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias e instalarlas
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Instalamos Gunicorn, el servidor de producción que pide la rúbrica
RUN pip install gunicorn

# Copiamos todo el código del proyecto al contenedor
COPY . /app/

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación con Gunicorn en vez del runserver de prueba
CMD ["gunicorn", "turismo_backend.wsgi:application", "--bind", "0.0.0.0:8000"]