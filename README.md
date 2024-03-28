# Flask RESTful API

This repository contains a Flask RESTful API project integrated with a MySQL database, providing a scalable solution for building web services.

## Features

- **RESTful Architecture**: Follows the REST architectural principles for designing APIs, allowing easy communication between client and server applications.
- **Flask Framework**: Utilizes Flask, a lightweight and flexible Python web framework, for rapid development of web services.
- **MySQL Database**: Integrates with a MySQL database for efficient data storage and retrieval, ensuring reliability and scalability.
- **Resource-Oriented Design**: Organizes endpoints around resources, providing a logical structure for handling API requests.
- **CRUD Operations**: Supports CRUD (Create, Read, Update, Delete) operations for managing resources in the database.

## Installation

1. Clone the repository:

   ```bash
   https://github.com/tusharmalankiya/flask-restful-api.git
   ```

2. Navigate to the project directory:

    ```bash
    cd flask-restful-api
    ```
3. Create a Python Virtual Environment:
```bash
python3 -m venv myenv
```

4. Activate the Virtual Environment:

-  On Unix or MacOS:
```bash
source myenv/bin/activate
```

- On Windows:
```bash
myenv\Scripts\activate
```

5. Install dependencies:
  ```bash
  pip3 install -r requirements.txt
  ```

4. Configure the database connection in *[db_config.py](https://github.com/tusharmalankiya/flask-restful-api/blob/main/db_config.py)*.

5. Run the application:
  ```bash
  python3 rest_api.py
  ```
The API will be accessible at http://localhost:6002/.


## Usage



- **Endpoint Documentation**: Access the API endpoint documentation and test endpoints using tools like Postman or curl.

- **Resource Manipulation**: Use HTTP methods (GET, POST, PUT, DELETE) to perform CRUD operations on resources.

## Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to improve the project.



