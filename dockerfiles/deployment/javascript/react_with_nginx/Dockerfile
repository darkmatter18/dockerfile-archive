# Stage 1: Build the React app
FROM node:22 as build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . ./

RUN npm run build

# Stage 2: Serve the React app with Nginx
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
