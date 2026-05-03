# Team Task Manager (Full-Stack Project)

A full-stack web application that allows users to manage projects, assign tasks, and track progress with role-based access control (Admin/Member).

---

##  Live Demo

 https://team-task-manager-izhn.onrender.com



##  GitHub Repository

 https://github.com/yuvsharm/team-task-manager

---

## Features

* User Authentication (Signup/Login with JWT)
* Role-Based Access (Admin / Member)
* Project Creation & Team Management
* Task Creation & Assignment
* Task Status Tracking (Pending / In Progress / Completed)
* Dashboard (Task progress & overdue tracking)



## Tech Stack

Backend:

* Django
* Django REST Framework

Authentication:

* JWT (SimpleJWT)

Database:

* SQLite (can be upgraded to PostgreSQL)

Deployment:

* Render

Server:

* Gunicorn

Static Files:

* Whitenoise



## API Overview

## Authentication

* `POST /api/signup/`
* `POST /api/login/`

## Projects

* `GET /api/projects/`
* `POST /api/projects/`

## Tasks

* `GET /api/tasks/`
* `POST /api/tasks/`
* `PATCH /api/tasks/{id}/`


## ⚙️ Local Setup

```bash
# Clone repository
git clone https://github.com/yuvsharm/team-task-manager.git

# Navigate to project
cd team-task-manager/clean-project

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```


## Deployment Note

The application was initially deployed on Railway as required.
However, due to persistent DNS issues (NXDOMAIN errors), the Railway deployment was not accessible.

To ensure a fully functional live application, the project is deployed on Render:

https://team-task-manager-izhn.onrender.com

---

## Demo

The demo includes:

* User Authentication
* Project Creation
* Task Assignment
* Role-based Access Control
* Dashboard Overview



 Author

Yuvraj Sharma
