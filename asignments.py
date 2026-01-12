from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, require_role
from app.models.assignment import Assignment
from app.utils.uploads import save_upload

router = APIRouter(prefix="/assignments", tags=["Assignments"])

@router.post("/submit")
def submit_assignment(
    subject: str,
    title: str,
    description: str | None = None,
    file: UploadFile = File(...),
    user=Depends(require_role("student")),
    db: Session = Depends(get_db)
):
    path = save_upload(file)
    assignment = Assignment(
        student_id=user.id,
        subject=subject,
        title=title,
        description=description,
        file_url=path
    )
    db.add(assignment)
    db.commit()
    return {"message": "Assignment submitted"}
