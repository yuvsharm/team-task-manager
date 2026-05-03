Team Task Manager (Full-Stack Project)

Live URL:
https://team-task-manager-izhn.onrender.com

GitHub Repository:
https://github.com/yuvsharm/team-task-manager

Project Overview:
This is a full-stack web application where users can create projects, assign tasks, and track progress with role-based access control (Admin/Member).

Key Features:

* User Authentication (Signup/Login using JWT)
* Role-based access (Admin / Member)
* Project creation and team management
* Task creation, assignment, and status tracking
* Dashboard for tracking task progress and overdue tasks

Tech Stack:

* Backend: Django, Django REST Framework
* Authentication: JWT (SimpleJWT)
* Database: SQLite (can be extended to PostgreSQL)
* Deployment: Render (Cloud Platform)
* Server: Gunicorn
* Static Handling: Whitenoise

API Features:

* Authentication APIs (Login / Signup)
* Project APIs (Create / Manage projects)
* Task APIs (Create / Assign / Update status)
* User Role Management

Deployment Note:
The application was initially deployed on Railway as required. However, due to persistent DNS issues (NXDOMAIN errors), the Railway domain was not accessible despite successful deployment.

To ensure a fully working live application, the project has been deployed on Render:
https://team-task-manager-izhn.onrender.com

All features are fully functional on the live deployment.

How to Run Locally:

1. Clone the repository
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Start server:
   python manage.py runserver

Demo:
The demo video showcases:

* User authentication
* Project creation
* Task assignment
* Role-based access
* Dashboard functionality

Author:
Yuvraj Sharma
