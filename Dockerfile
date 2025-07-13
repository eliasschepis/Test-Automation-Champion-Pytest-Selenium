# Usa una imagen base con Python preinstalado
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta los tests cuando el contenedor se inicie
CMD ["pytest", "--html=reports/report.html", "--self-contained-html"]

# Una vez completo, correr esto en terminal "docker build -t qa-automation-framework ." // Esto construye una imagen llamada qa-automation-framework con tu proyecto.
# Y luego "docker run --rm -v ${PWD}/reports:/app/reports qa-automation-framework" // para ejecutar el contenedor