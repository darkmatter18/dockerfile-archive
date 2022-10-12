**Dockerizing a Node.js web app**



File Structure:
package.json file => describes app and its dependencies
server.js file => defines a web app using the Express.js framework
Dockerfile

#Build Image:
docker build . -t <your docker username>/node-web-app

#Run Container using image:
docker run -p 49160:8080 -d <your username>/node-web-app

#Go inside the container:
docker exec -it <container id> /bin/bash

#Test the container is creted or not

docker ps
OR
curl -i localhost:49160
