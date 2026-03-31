FROM nginx:alpine

# Copy static files to Nginx html directory
COPY . /usr/share/nginx/html

# custom nginx config to handle proxying /api to the backend
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
