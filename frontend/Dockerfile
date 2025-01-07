# Imagen base para React con TypeScript
FROM node:18-alpine

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de configuración y dependencias
COPY package.json package-lock.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del código fuente
COPY . .

# Construir la aplicación para producción
RUN npm run build

# Usar un servidor estático para servir los archivos
RUN npm install -g serve

# Exponer el puerto 3000
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["serve", "-s", "dist"]
