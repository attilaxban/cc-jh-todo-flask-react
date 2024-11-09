
# Flask TODO Application

A simple Flask application that manages a TODO list using PostgreSQL as the database. This application allows users to create, read, update, and delete TODO items through a RESTful API.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running the Backend](#running-the-backend)
- [Running the Frontend](#running-the-frontend)

## Features

- Create new TODO items
- Retrieve the list of TODO items
- Update the status of existing TODO items
- Delete TODO items

## Technologies Used

- **Python**: Programming language used for the backend.
- **React-Vite + Javascript** : Programming language used for the frontend.
- **Flask**: Web framework for building the API.
- **PostgreSQL**: Database management system to store TODO items.
- **psycopg2**: PostgreSQL adapter for Python.
- **dotenv**: To manage environment variables.
- **Docker**: The application is containerized so you can run the full application with ***docker compose up -d --build*** command
- **GitHub Action**: Push request triggers the action to run some http test with HTTPie

## Installation

1. **Clone the repository**:

2. **Install dependencies**:

   All necessary dependencies for this project are listed in the `requirements.txt` file. To install them, you can use `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration**:

   Before running the application, you need to set up your PostgreSQL database credentials. Create a `.env` file in the root of your project directory with the following content:

   ```plaintext
   USER_NAME=your_database_username
   PASSWORD=your_database_password
   ```

## Backend Setup

This backend is built using Flask and communicates with a PostgreSQL database to manage TODO items. Below are the instructions for setting up the backend.

### Database Initialization

The application includes a script that will automatically create the necessary database and table if they do not exist. Upon running the backend for the first time, it will drop the existing `todos` table (if any) and create a new one with the necessary fields.

### Running the Backend

To start the Flask application, run the following command in your terminal:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
By default, the app will run on `http://0.0.0.0:4000`. You can access the API at the following endpoints or you can use the test requests from test.http with a REST Client:

- `GET /api/v1/todos`: Retrieve the list of TODO items.
- `POST /api/v1/create`: Create a new TODO item.
- `PATCH /api/v1/update`: Update the status of an existing TODO item.
- `DELETE /api/v1/delete`: Delete a TODO item.

### Running the Frontend

To start the frontend run the following command in your terminal:

 ```bash
 cd frontend
 npm install
 npm run dev
 ```

 ### Run the Application with docker-compose:

 To start the application with docker compose run the following command in your terminal:

 ```bash
 docker compose up -d --build
 ```

### Important Notes

- Ensure your PostgreSQL server is running and accessible at `localhost` on port `5432`.
- The application runs in debug mode (`debug=True`), which is helpful for development but should be turned off in a production environment.
- Make sure you have the necessary permissions to create tables in your PostgreSQL database.

## API Endpoints

Here’s a quick overview of the available API endpoints:

- **GET /api/v1/todos**: Retrieves all TODO items.
- **POST /api/v1/create**: Adds a new TODO item.
  - Request body should contain JSON data with the key `todo`.
- **PATCH /api/v1/update**: Updates the completion status of a TODO item.
  - Request body should contain JSON data with keys `todo` (the TODO item's name) and `isFinished` (boolean value).
- **DELETE /api/v1/delete**: Deletes a TODO item.
  - Request body should contain JSON data with the key `id` (the TODO item ID)..


  