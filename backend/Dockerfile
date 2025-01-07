# Base image for Python
FROM python:3.10-slim

# Instalar dependencias necesarias para SQL Server
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    curl \
    gnupg && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql17 \
    mssql-tools && \
    apt-get clean

# Agregar herramientas al PATH
ENV PATH="/opt/mssql-tools/bin:$PATH"


# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port and run
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
