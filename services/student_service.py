# services/student_service.py

from database.mongo_client import get_db


def find_students_by_name(name_query: str):
    """
    Finds students by name (case-insensitive).
    Returns:
        - [] if no match
        - list of students if matches found
    """
    db = get_db()

    query = {
        "name": {"$regex": name_query, "$options": "i"}
    }

    return list(db.students.find(query))


def get_student_profile(name_query: str):
    """
    Returns:
    - dict (student profile) if exactly one match
    - dict with 'error' message otherwise
    """
    matches = find_students_by_name(name_query)

    if len(matches) == 0:
        return {"error": "No student found with that name."}

    if len(matches) > 1:
        return {
            "error": "Multiple students found.",
            "candidates": [s["name"] for s in matches]
        }

    student = matches[0]

    return {
        "student_id": student["_id"],
        "name": student["name"],
        "grade": student["grade"],
        "section": student["section"],
        "roll_no": student["roll_no"],
        "parents": student["parent_details"],
        "transport": student["logistics"]
    }
