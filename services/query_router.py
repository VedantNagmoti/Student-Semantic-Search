# services/query_router.py

from services.student_service import get_student_profile
from services.academic_service import get_academic_record
from services.curriculum_service import get_curriculum_by_grade
from services.school_info_service import (
    get_transport_route,
    get_school_policies,
    get_school_calendar
)


def route_query(query: str):
    """
    Very simple rule-based router (initial version).
    """

    q = query.lower()

    # -------- Student Profile --------
    if "details" in q or "profile" in q:
        name = query.split("of")[-1].strip()
        return get_student_profile(name)

    # -------- Attendance / Marks --------
    if "attendance" in q or "marks" in q or "performance" in q:
        name = query.split("of")[-1].strip()
        student = get_student_profile(name)

        if "error" in student:
            return student

        return get_academic_record(student["student_id"])

    # -------- Curriculum --------
    if "syllabus" in q or "timetable" in q:
        for token in q.split():
            if token.isdigit():
                return get_curriculum_by_grade(int(token))

    # -------- Transport --------
    if "route" in q:
        for token in query.split():
            if token.startswith("Route"):
                return get_transport_route(token)

    # -------- Policies --------
    if "fee" in q or "uniform" in q or "policy" in q:
        return get_school_policies()

    # -------- Calendar --------
    if "holiday" in q or "calendar" in q:
        return get_school_calendar()

    return {"error": "Query not understood yet."}
