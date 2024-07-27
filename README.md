# awareSatisfactory

This is the ERP project for Satisfactory game called awareSatisfactory. This README provides an overview of the folder structure and purpose of each file and directory in the project.

## Folder Structure
`awareSatisfactory/`<br/>
`├── backend/`<br/>
`│ ├── app/`<br/>
`│ │ ├── init.py`<br/>
`│ │ ├── main.py`<br/>
`│ │ ├── models.py`<br/>
`│ │ ├── schemas.py`
`│ │ ├── crud.py`
`│ │ ├── database.py`
`│ ├── requirements.txt`
`│ ├── data/`
`│ │ ├── users.json`
`│ ├── gunicorn_conf.py`
`├── frontend/`
`│ ├── app.py`
`│ ├── requirements.txt`
`├── .gitignore`
`├── README.md`


## Description of Files and Directories

### Root Directory (`satisfactory-web-app/`)

- **.gitignore**: Specifies files and directories that should be ignored by Git.
- **README.md**: Provides an overview and documentation for the project.

### Backend Directory (`backend/`)

- **app/**: Contains the main application code for the backend.
  - **\_\_init\_\_.py**: Initializes the `app` package.
  - **main.py**: Entry point for the backend application, contains FastAPI app setup.
  - **models.py**: Defines data models and schemas for the application.
  - **schemas.py**: Contains Pydantic schemas for data validation and serialization.
  - **crud.py**: Implements CRUD (Create, Read, Update, Delete) operations for the application.
  - **database.py**: Manages interactions with the data storage (currently using JSON files).
- **requirements.txt**: Lists the Python dependencies required for the backend.
- **data/**: Stores JSON files used as data storage for the application.
  - **users.json**: Sample JSON file for storing user data.
- **gunicorn_conf.py**: Configuration file for running the backend with Gunicorn.

### Frontend Directory (`frontend/`)

- **app.py**: Entry point for the frontend application.
- **requirements.txt**: Lists the Python dependencies required for the frontend.



