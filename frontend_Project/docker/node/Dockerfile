FROM node:18-alpine

# Install Nginx and OpenSSL
RUN apk update && \
    apk add nginx openssl && \
    rm -rf /var/cache/apk/*

# Create SSL directory
RUN mkdir -p /etc/nginx/ssl/

# Generate self-signed SSL certificate
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/key.pem -out /etc/nginx/ssl/cert.pem \-subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=localhost"

# Set working directory
WORKDIR /app

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]