# React with Nginx Docker Setup

This project demonstrates how to set up a React application with Nginx using Docker and Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/react-nginx-docker.git
    cd react-nginx-docker
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

3. Open your browser and navigate to `http://localhost` to see your React app.

## Project Structure

- `Dockerfile`: Defines the Docker image for building and serving the React app.
- `nginx.conf`: Configuration file for Nginx to serve the React app.
- `docker-compose.yml`: Manages the services using Docker Compose.
- `README.md`: Provides instructions for setting up and running the project.

## Notes

- The React app is built using a multi-stage Docker build to optimize the final image size.
- Nginx is configured to serve the React app and handle client-side routing.

## Useful Commands

- To stop the Docker containers:

    ```bash
    docker-compose down
    ```

- To rebuild the Docker images without using the cache:

    ```bash
    docker-compose build --no-cache
    ```

- To view logs from the Docker containers:

    ```bash
    docker-compose logs -f
    ```

## License

This project is licensed under the MIT License.
