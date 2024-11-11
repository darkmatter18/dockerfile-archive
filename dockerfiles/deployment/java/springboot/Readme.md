# Dockerizing a Spring Boot Application

this guide provides a detailed instructions on how to build and run a docker image for a springboot application using a custom dockerfile and a docker compose. multi-stage build was used to optimize the imag size by separating the build-time dependencies from the runtime dependencies. Docker compose is to simplify the complexity associated with container management.

####  File Structure
. app: Spring boot application code
  . src: source code directory
  . pom.xml or build.gradle: build configuration for maven or gradle
. Dockerfile: the docker image build instructions
. docker-compose.yml: the docker compose file

#### Prerequisites
you are expected to have the following;
. docker installed on your machine
. a spring boot application to be dockerized
. a pom.xml or build.gradle file for maven or gradle
. docker compose installed on machine.

## Overview of the Dockerfile
### Maven
. multi-stage build
#### First Stage
. installs maven to build the application
. copies the pom.xml and runs mvn dependency:go-offline to cache dependencies
. copies the source code and packages the application

#### Second Stage
. includes the JRE(from amazon corretto JDK 21)
. copies the packaged JAR from the build stage
. sets the entrypoint to run the application.

### Gradle
#### First Stage
. Build the application
   . uses debian:bookworm-slim as base image
   . installs necessary packages
   . installs amazon corretto jdk
   . updates package lists and installs jdk
   . removes the unnecessary packages and cleans the package lists to save space
   . set JAVA_HOME environment variable
   . installs gradle
   . sets working directory
   . copy build scripts and configurations
   . downloads dependencies
   . copys source code
   . builds the application

   #### Second Stage
   . uses debian:bookworm-slim as base image 
   . installs amazone corretto jdk 21
   . sets JAVA_HOME environment variable
   . sets working directory
   . copys the application JAR from the build stage
   . expose Port 8080
   . runs the application



## Overview of the docker-compose file
if your application ultilizes a database it is best to run it with  docker-compose. 
The below docker-compose assumes your database is postgres.
Below is an overview of the docker-compose file

. version: this states the version of the docker compose file
. services: this is the services to run
  . app: name of service
  . build: builds the docker image from the Dockerfile in current context(please replace with the path of your dockerfile)
  . ports: maps port 8080 of the host port 8080 of the container
  . environment: sets the environment variables inside the container.
  . restart: restarts the container unless it is explicitly stopped.
  . depends_on: specifices service dependencies
  . db: defines the database services
  . volumnes: persists data on the host machine.

  ## Build and Run the Docker Image with Docker Compose
  1. build and run the application

  ``` docker-compose up -d```
  2. verify that the containers are running

  ```docker-compose ps```
  3. Access your application at 
  ``` http://localhost:8080 ```
  4. Stop and Remove Contaiiners
  ``` docker-compose down ```
  5. View Logs
  ``` docker-compose logs -f ```
  6. Rebuildiing the image
  ``` docker-compose up -d --build ```
  7. To access container shell
  ``` docker-compose exec app /bin/bash ```
  




