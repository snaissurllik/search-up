# SearchUp

This is a project written in Python Django, Rest Framework. Main database - Postgres , Redis is used as a secondary database and cache storage. The project is containerized using Docker and Docker Compose.

## Getting Started

### Prerequisites

Before you can use this project, you will need to have the following installed on your system:

- Docker
- Docker Compose

### Installation

1. Clone the repository to your local machine: git clone https://github.com/snaissurllik/search-up.git

2. Generate a secret key for your Django project by running the following command: python secret_key_generator.py

3. Create .env file in the root project directory and specify environment variables listed in .env-template. Copy generated secret key to SECRET_KEY variable. Note that DB_USER, DB_PASSWORD, DB_NAME varibales can be freely set to any values and Postgres container will automatically create database using given credentials.

4. Start the Docker containers by running the following command: docker-compose up --build

5. Populate the database with countries and regions by running the following command: docker-compose exec django python load_geo.py

6. Open your web browser and navigate to `http://localhost:8000/account/login` to access the web application.

7. To create a superuser (admin), use the following command: docker-compose exec django python manage.py createsuperuser

