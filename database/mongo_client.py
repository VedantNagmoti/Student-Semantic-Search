# database/mongo_client.py

from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

_client = None
_db = None


def get_db():
    """
    Returns a singleton MongoDB database connection.
    """
    global _client, _db

    if _db is None:
        _client = MongoClient(MONGO_URI)
        _db = _client[DB_NAME]

    return _db
