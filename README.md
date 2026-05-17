# Job Tracker API

This is a simple backend project built using Flask to track job applications. It allows users to register, login, and manage their job applications in one place.

---

## What this project does

- Users can create an account and log in
- After login, a JWT token is generated for authentication
- Users can add job applications (company, role, status)
- Users can update job status (Applied, Interview, Selected, Rejected)
- Users can delete job applications
- Users can search jobs by company or status
- Each user can only access their own job data

---

## Tech Stack

- Python
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- SQLite
- Postman (for API testing)

---

## API Endpoints

### Authentication
- POST /register → Create a new user
- POST /login → Login and get JWT token

### Jobs
- POST /jobs → Add a job
- GET /jobs → Get all jobs
- PUT /jobs/<id> → Update job
- DELETE /jobs/<id> → Delete job
- GET /jobs/search → Search jobs by company or status

## How to run this project
pip install -r requirements.txt
python app.py

Note:
I built this project to understand backend development, REST APIs, authentication using JWT, and database handling using SQLAlchemy.


