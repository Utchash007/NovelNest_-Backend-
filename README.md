# NovelNest Backend

This repository contains the backend of the full-stack web application **NovelNest**. It is built using **Python Django** and **Django REST Framework** to handle data and business logic efficiently.

---

## Features

- **Django Backend**:
  - Provides RESTful APIs via Django REST Framework.
  - Handles data processing, business logic, and database interactions seamlessly.
  
- **Cross-Origin Support**:
  - Uses `django-cors-headers` for enabling cross-origin resource sharing.

- **Database Integration**:
  - Compatible with MySQL database using `mysqlclient`.

---

## Requirements

- Django: 5.1.4
- django-cors-headers: 4.6.0
- djangorestframework: 3.15.2
- mysqlclient: 2.2.6
- pip: 24.3.1
- Python: 3.12.8

---

## Setup Instructions

Follow these steps to set up the backend locally:

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd novelnest-backend
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install django django-cors-headers djangorestframework mysqlclient
    ```

4. **Configure the Database**:
    - Update the `DATABASES` configuration in `settings.py` with your MySQL credentials.

5. **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Start the Development Server**:
    ```bash
    python manage.py runserver
    ```

The backend will be available at `http://127.0.0.1:8000/` by default.

---