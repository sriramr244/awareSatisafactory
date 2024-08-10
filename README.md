# awareSatisfactory

This is the ERP project for Satisfactory game called awareSatisfactory. This README provides an overview of the folder structure and purpose of each file and directory in the project.

# Frontend Directory Structure

awareSatisfactory/<br/>
├── backend/<br/>
│ ├── app/<br/>
│ │ ├── init.py<br/>
│ │ ├── main.py<br/>
│ │ ├── models.py<br/>
│ │ ├── schemas.py<br/>
│ │ ├── crud.py<br/>
│ │ ├── database.py<br/>
│ ├── requirements.txt<br/>
│ ├── data/<br/>
│ │ ├── users.json<br/>
│ ├── gunicorn_conf.py<br/>
├── frontend/<br/>
│ ├── public/<br/>
│ │ ├── index.html <br/>
│ │ ├── Other static files<br/>
│ ├── src/<br/>
│ │ ├── components/<br/>
│ │ │ ├── Sidebar.js <br/>
│ │ ├── pages/<br/>
│ │ │ ├── AddInventory.js <br/>
│ │ │ ├── AnotherTab.js <br/>
│ │ │ ├── Home.js <br/>
│ │ ├── App.js <br/>
│ │ ├── index.js <br/>
│ │ ├── reportWebVitals.js<br/>
│ │ ├── setupTests.js <br/>
│ ├── .env <br/>
│ ├── package.json <br/>
│ ├── README.md <br/>
├── .gitignore<br/>
├── README.md<br/>


## Description of Files and Directories

### Root Directory (`awareSatisfactory/`)

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

- **public/**: Contains static assets that are served directly by the web server.
  - **index.html**: The main HTML file that serves as the entry point for the React application. It contains a `<div>` with an `id="root"` where the React app mounts.
  - **Other static files**: Such as images, icons, and other static resources.
- **src/**: Contains the source code for the React application.
  - **components/**: Contains reusable components that can be used throughout the application.
    - **Sidebar.js**: A sidebar component that provides navigation links to different parts of the application.
  - **pages/**: Contains the main page components of the application, each representing a different route.
    - **AddInventory.js**: This component handles the functionality for adding inventory. It includes a form for inputting item name and quantity and sends this data to the backend API.
    - **AnotherTab.js**: This is a placeholder component for another tab in the application. It can be customized to display any content.
    - **Home.js**: This component displays the home page, which dynamically lists all available tabs by fetching data from the backend API.
  - **App.js**: The main application component that sets up the routing and includes the `Sidebar` and the different pages. It uses `react-router-dom` for client-side routing.
  - **index.js**: The entry point for the React application. It renders the `App` component into the DOM. It also includes the call to `reportWebVitals`.
  - **reportWebVitals.js**: This file is used to measure the performance of the application. It is optional and can be customized or removed based on your needs.
  - **setupTests.js**: This file is used for setting up testing configurations. It is usually used to configure Jest and other testing libraries.
- **.env**: This file contains environment variables used by the React application. For example, the backend API URL can be defined here.
- **package.json**: This file contains metadata about the project and lists dependencies and scripts for building and running the application.
- **README.md**: This file provides an overview of the project, instructions on how to set it up, and any other relevant information for developers.
### Languages chosen
- **Backend**: Python
- **Frontend**: JavaScript (React)
  
## Frameworks chosen
- **Backend**: FastAPI
- **Frontend**: React
## Database
- **Local JSON** (for now, but planning MongoDB for future)



