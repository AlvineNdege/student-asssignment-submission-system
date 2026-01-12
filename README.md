📘 Student Assignment Submission System
Project Overview

The Student Assignment Submission System is a secure, role-based backend application that enables students to submit assignments and teachers to review, comment on, and grade them. The system is designed using modern backend technologies and follows industry best practices.

Core Features

Role-based access control (Student, Teacher, Admin)

Secure JWT authentication (access & refresh tokens)

Assignment submission with file uploads

Assignment review, commenting, and grading

Assignment status lifecycle (submitted → reviewed → graded)

Pagination, sorting, and filtering

Automatic API documentation (Swagger/OpenAPI)

Technology Stack

Framework: FastAPI

Database: PostgreSQL (MySQL compatible)

ORM: SQLAlchemy

Migrations: Alembic

Authentication: JWT

File Storage: Local filesystem (/uploads)

Configuration: .env environment variables

User Roles

Student: Submit and view own assignments

Teacher: Review, comment, and grade assignments

Admin (optional): System oversight

Security

Password hashing using bcrypt

JWT-protected endpoints

Role-based authorization enforcement

Sensitive configuration stored in environment variables

Running the Project
uvicorn app.main:app --reload


API Documentation:

Swagger UI: http://localhost:8000/docs
