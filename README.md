# Job Tracker API

This is a backend project built using Flask to track and manage job applications. It allows users to register, login, and securely manage their job applications in one place using JWT authentication.

---

## What this project does

- Users can register and log in securely
- JWT token is generated for authentication
- Users can add job applications (company, role, status)
- Users can update job status (Applied, Interview, Selected, Rejected)
- Users can delete job applications
- Users can search jobs by company or status
- Each user can only access their own job data
- Follow-up reminder system added for job tracking

---

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite
- Postman (for API testing)

---

## API Endpoints

### Authentication

- POST /register → Create a new user
- POST /login → Login and get JWT token

### Jobs

- POST /jobs → Add a new job
- GET /jobs → Get all jobs for logged-in user
- PUT /jobs/<id> → Update job details
- DELETE /jobs/<id> → Delete a job
- GET /jobs/search → Search jobs by company or status

---

## Job Reminder Feature

Each job can include a follow-up date. The system automatically calculates:

- Days left for follow-up
- Whether a reminder is due or not

---

## How to run this project

```bash id="run1"
pip install -r requirements.txt
python app.py

Note:
I built this project to understand backend development, REST APIs, authentication using JWT, and database handling using SQLAlchemy.


```
