# Utilizamos la imagen ligera de Python
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Permitir que las declaraciones y los mensajes de registro aparezcan inmediatamente en los registros de Knative
ENV PYTHONUNBUFFERED True

# Copiamos el c�digo local al contenedor
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Instalamos el servidor para que pueda correr nuestra aplicaci�n 
RUN pip install Flask gunicorn

# Ejecute el servicio web al iniciar el contenedor. Aqu� usamos el gunicorn
# servidor web, con un proceso de trabajo y 8 subprocesos.
# Para entornos con varios n�cleos de CPU, aumente la cantidad de trabajadores
# para ser igual a los n�cleos disponibles.
# El tiempo de espera se establece en 0 para deshabilitar los tiempos de espera de los trabajadores para permitir que Cloud Run maneje el escalado de instancias.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

# [END run_helloworld_dockerfile]
# [END cloudrun_helloworld_dockerfile]
