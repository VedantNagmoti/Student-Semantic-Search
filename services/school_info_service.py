# services/school_info_service.py

from database.mongo_client import get_db


def get_transport_route(route_id: str):
    """
    Fetch transport route details.
    """
    db = get_db()

    doc = db.school_info.find_one(
        {
            "category": "transport",
            "routes.route_id": route_id
        },
        {"_id": 0}
    )

    if not doc:
        return {"error": "Transport route not found."}

    for route in doc["routes"]:
        if route["route_id"] == route_id:
            return route

    return {"error": "Transport route not found."}


def get_school_policies():
    """
    Fetch all school policies.
    """
    db = get_db()

    policies = list(
        db.school_info.find(
            {"category": "policies"},
            {"_id": 0}
        )
    )

    return policies


def get_school_calendar():
    """
    Fetch academic calendar.
    """
    db = get_db()

    calendar = db.school_info.find_one(
        {"category": "calendar"},
        {"_id": 0}
    )

    if not calendar:
        return {"error": "School calendar not found."}

    return calendar["events"]
