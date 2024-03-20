# Recipe API

This project provides a Django Rest Framework (DRF) API for managing cooking recipes, ingredients, and tags.

## Getting Started

Follow the steps below to set up the project.

### Prerequisites  
  
- Python 3.10+  
- Pip (Python package manager)  
- Docker, Docker Compose (for containerization) 

### Installation 
1. Clone the repository:

    ```bash
    git clone https://github.com/Ence1ad/recipe-api 
    ```
2. Navigate to the project directory: 
  
    ```bash  
    cd recipe-api
    ```  
3. Create an .env file based on the provided .env.example:

    ```bash  
    cp .env.example .env
    ``` 
4. Open the .env file in a text editor and fill in the required configuration values. 

    ```env
    # Database Configuration
    POSTGRES_USER= # PostgreSQL database superuser.  
    POSTGRES_PASSWORD= # Password for the PostgreSQL database superuser.
    ...
    # DRF Configuration
    DJANGO_SECRET_KEY=change_me
    ALLOWED_HOSTS=127.0.0.1
    ```
5. Ensure you have both Docker and Docker Compose installed:

   - [Install Docker](https://docs.docker.com/get-docker/)
   - [Install Docker Compose](https://docs.docker.com/compose/install/)

6. Build the Docker image and start the services using Docker Compose:

    ```bash  
    docker compose -f docker-compose-deploy.yml up --build
    ```
7. To stop all the Docker containers, simply run:

   ```bash  
    docker compose down --remove-orphans
    ```

## Authentication

The API uses Token-based authentication. To access authenticated endpoints, users need to include their authentication token in the request headers.

## API Documentation

The API documentation can be found at `/api/schema/swagger-ui/`, which provides an interactive interface for exploring and testing the API endpoints.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request with any improvements or features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.