# awareSatisfactory Backend

This is the backend component of the awareSatisfactory ERP project for the Satisfactory game. This README provides an overview of the folder structure, purpose of each file, and instructions on how to set up and run the backend.

## Backend Directory Structure

awareSatisfactory/backend/<br/>
├── app/<br/>
│ ├── \_\_init\_\_.py<br/>
│ ├── main.py<br/>
│ ├── models.py<br/>
│ ├── schemas.py<br/>
│ ├── crud.py<br/>
│ ├── database.py<br/>
├── requirements.txt<br/>
├── data/<br/>
│ ├── users.json<br/>
├── gunicorn_conf.py<br/>
├── tests/<br/>
│ ├── test_schema.py<br/>
│ ├── \_\_init\_\_.py<br/>
├── .gitignore<br/>
├── README.md<br/>

## Description of Files and Directories

### Root Directory (`backend/`)

- **.gitignore**: Specifies files and directories that should be ignored by Git.
- **README.md**: Provides an overview and documentation for the backend project.

### `app/` Directory

Contains the main application code for the backend.

- **\_\_init\_\_.py**: Initializes the `app` package.
- **main.py**: Entry point for the backend application, contains FastAPI app setup.
- **models.py**: Defines data models and schemas for the application.
- **schemas.py**: Contains Pydantic schemas for data validation and serialization.
- **crud.py**: Implements CRUD (Create, Read, Update, Delete) operations for the application.
- **database.py**: Manages interactions with the data storage (currently using JSON files).

### `data/` Directory

Stores JSON files used as data storage for the application.

- **users.json**: Sample JSON file for storing user data.

### `tests/` Directory

Contains test cases for the application.

- **test_schema.py**: Defines tests for the GraphQL schema.
- **\_\_init\_\_.py**: Ensures the directory is treated as a Python package.

### Other Files

- **requirements.txt**: Lists the Python dependencies required for the backend.
- **gunicorn_conf.py**: Configuration file for running the backend with Gunicorn.

## How to Run the Backend

To set up and run the backend server, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd awareSatisfactory/backend
2. **Create virtural environment:**
    ```sh
    python3.10 -m venv benv
4. **Activate the virtual environment:**
   ```sh
   source benv/bin/activate
3. **Install Dependancies:**
    ```sh
    pip install -r requirements.txt
5. **Run the Application:***
   ```sh
   benv/bin/uvicorn app.mainapp --reload

## Access the API
  Open your browser and direct to http://localhost:8000
### GraphQL Playground
  Access the graphQL playground at http://localhost:8000/graphql
### Access Swagger docs:
  FastAPI automatically generates interactive API documentation using Swagger UI. Access it at http://localhost:8000/docs.

## Running the tests
To run the tests, follow these steps:
1. Ensure your virtual environment is activated.
2. Run the tests using pytest:
   ```sh
   pytest

This will discover and run all the tests in the tests directory.

# Contributing
If you wish to contribute to the project, please fork the repository, create a new branch, and submit a pull request. Ensure your code follows the project's coding standards and includes relevant tests.
