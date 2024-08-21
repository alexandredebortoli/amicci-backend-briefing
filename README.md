# Amicci - Practical Test for BackEnd Developer

Objective: Create an API for briefing consultation.
This project is a Restful API built with Django and Django Rest Framework, using PostgreSQL as the database, all containerized with Docker.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Create a `.env` file in the project root, using the `.env-example` file as a reference. This file should contain the necessary environment variables for the application.

## How to Run

To run the project, use Docker Compose with the following command:

``` bash
docker-compose -f docker-compose.dev.yml up --build -d
```

This will build the images and start the containers for the API application and the PostgreSQL database.

## Available Endpoints

The API has the following endpoints for the available collections: **categories**, **vendors**, **retailers**, and **briefings**.

> Note: Make sure `Content-Type: application/json` is set on request `Headers`

Base API Route: `/api/demo/`

#### Categories

- GET `/api/demo/categories`: Lists all categories.
- GET `/api/demo/categories/{id}`: Retrieves a specific category.
- POST `/api/demo/categories`: Creates a new category.
- PUT `/api/demo/categories/{id}`: Updates an existing category.

#### Vendors

- GET `/api/demo/vendors`: Lists all vendors.
- GET `/api/demo/vendors/{id}`: Retrieves a specific vendor.
- POST `/api/demo/vendors`: Creates a new vendor.
- PUT `/api/demo/vendors/{id}`: Updates an existing vendor.

#### Retailers

- GET `/api/demo/retailers`: Lists all retailers.
- GET `/api/demo/retailers/{id}`: Retrieves a specific retailer.
- POST `/api/demo/retailers`: Creates a new retailer.
- PUT `/api/demo/retailers/{id}`: Updates an existing retailer.

#### Briefings

- GET `/api/demo/briefings`: Lists all briefings.
- GET `/api/demo/briefings/{id}`: Retrieves a specific briefing.
- POST `/api/demo/briefings`: Creates a new briefing.
- PUT `/api/demo/briefings/{id}`: Updates an existing briefing.

## Database

The database used is PostgreSQL, running in a Docker container along with the application.

**To run only the database in docker:**

``` bash
docker-compose -f docker-compose.dev.yml up -d db
```