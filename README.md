# User Management Application

A Flask-based web application for collecting and managing user information with a MySQL database backend, containerized using Docker.

## Features

- **User Input Form**: Collect user details including name, phone number, email, age, and sex
- **Database Storage**: Persistent storage using MySQL
- **REST API**: JSON endpoints for data retrieval
- **Dockerized**: Easy deployment with Docker Compose

## Architecture

- **Frontend**: HTML form with CSS styling
- **Backend**: Flask web framework
- **Database**: MySQL 8
- **Containerization**: Docker and Docker Compose

## Prerequisites

- Docker
- Docker Compose

## Installation and Setup

1. **Clone the repository** (if applicable) or navigate to the project directory:

   ```
   cd "d:\Devops_Projects\devops network"
   ```

2. **Build and start the services**:

   ```
   docker-compose up --build
   ```

   This will:

   - Build the Flask application container
   - Start MySQL database
   - Initialize the database schema
   - Start the web server on port 5000

3. **Wait for initialization**:
   The application will automatically initialize the database when first accessed. The healthcheck ensures MySQL is ready before the app starts.

## Usage

### Accessing the Application

- **User Form**: Visit `http://localhost:5000/form` in your web browser
- **API Endpoint**: Visit `http://localhost:5000/users` for JSON data of all users

### Frontend Interface

The user input form includes:

- Name (text field)
- Phone Number (text field)
- Email (email field with validation)
- Age (number field)
- Sex (dropdown: Male, Female, Other)
- Save button

![Frontend Form](frontend-screenshot.png)

_Note: Add a screenshot of the form here by taking a picture of the page at `/form` and saving it as `frontend-screenshot.png` in the project root._

### API Endpoints

- `GET /`: Home page with status message
- `GET /form`: User input form
- `POST /save`: Save user data (redirects to form)
- `GET /users`: Retrieve all users as JSON

## Database Schema

The `users` table includes:

- `id` (INT, Primary Key, Auto Increment)
- `name` (VARCHAR(255))
- `phone_number` (VARCHAR(20))
- `email` (VARCHAR(255))
- `age` (INT)
- `sex` (VARCHAR(10))

## Development Workflow

1. **Make changes** to the code (app.py, templates, etc.)
2. **Rebuild containers**:
   ```
   docker-compose up --build
   ```
3. **Test changes** by accessing the application
4. **Check logs** if issues arise:
   ```
   docker-compose logs
   ```

## Stopping the Application

```
docker-compose down
```

## Troubleshooting

- **Port 5000 already in use**: Stop other services using port 5000
- **Database connection errors**: Ensure Docker is running and wait for MySQL healthcheck
- **Form not loading**: Check browser console for errors and verify containers are running with `docker-compose ps`

## Technologies Used

- Python 3.10
- Flask 3.1
- MySQL 8
- MySQL Connector Python
- Docker
- Docker Compose

## Project Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker build configuration
├── docker-compose.yml    # Multi-container setup
├── templates/
│   └── form.html         # User input form template
└── README.md             # This file
```
