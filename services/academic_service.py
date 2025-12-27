# services/academic_service.py

from database.mongo_client import get_db


def get_academic_record(student_id: str):
    """
    Fetch academic performance for a student.
    """
    db = get_db()

    record = db.academic_records.find_one(
        {"student_id": student_id},
        {"_id": 0}
    )

    if not record:
        return {"error": "No academic record found."}

    return {
        "academic_year": record["academic_year"],
        "class_teacher": record["class_teacher"],
        "attendance": record["attendance_summary"],
        "marks": record["grade_card"],
        "pending_assignments": record["pending_assignments"]
    }
