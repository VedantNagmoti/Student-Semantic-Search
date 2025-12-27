# main.py

from database.mongo_client import get_db

db = get_db()
collections = db.list_collection_names()

print("Connected to DB successfully!")
print("Collections:", collections)
