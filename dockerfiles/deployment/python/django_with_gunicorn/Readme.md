# Dockerizing a Python-Django Application with Gunicorn

This document is a guide on how to build and run a docker image for a python Django web  application using Gunicorn and a multi-stage docker build. We ultilize the multi-stage approache so that we can optimize the image size by separating the build-time dependencies from runtime dependencies.

## File Structure
- app: python application code
   - wsgi.py: the wsgi entry point for the application
- requirements.txt: python package dependencies for the application
- Dockerfile: The docker image build process.

## Prerequisites
- Docker software installed on your machine
- the python/django application you plan to dockerize
- A requiremrnts.txt file

## Overview of Dockerfile
the dockerfile uses two stages
1. build stage: this builds the python wheel packages
2. final stage: copies and installs the wheels

## Build and Run the docker image
1. build the image
``` docker build -t <image-name> .```
2. Run the docker container
``` docker run -p <host_port:container_port> -d <image-name> ```
   - -p publishes container port to host port
   - -d runs the container in a detached mode.
3. Verify runing container
``` docker ps ```
4. Access your Application on the browser or do 
``` curl http://localhost:<host_port> ``` on your terminal
5. Access container shell
``` docker exec -it <container_id> /bin/bash ```
6. Stop container
``` docker stop <container_id> ```
7. Remove container
``` docker rm <container_id> ```





