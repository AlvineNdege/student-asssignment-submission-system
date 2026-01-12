from fastapi import FastAPI
from app.api import auth, assignments

app = FastAPI(
    title="Student Assignment Submission System",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(assignments.router)
