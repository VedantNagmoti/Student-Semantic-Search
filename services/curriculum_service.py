# services/curriculum_service.py

from database.mongo_client import get_db


def get_curriculum_by_grade(grade: int):
    """
    Fetch curriculum details for a class.
    """
    db = get_db()

    curriculum = db.curriculum.find_one(
        {"grade": grade},
        {"_id": 0}
    )

    if not curriculum:
        return {"error": "No curriculum found for this grade."}

    return {
        "grade": curriculum["grade"],
        "syllabus": curriculum.get("syllabus"),
        "timetable": curriculum.get("timetable"),
        "exam_datesheet": curriculum.get("exam_datesheet")
    }
