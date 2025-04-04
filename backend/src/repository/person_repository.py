import db.db_access_manager as db
from fastapi import HTTPException, status

def get_contact_persons(person_id):
    query = """
    SELECT role FROM student_mentor WHERE personId = %s
    """
    params = (person_id)
    results = db.fetch_query_results_as_dict(query, params)
    res = []
    for result in results:
        res.append(result["role"])


def get_students(field, value):
    query = """
    SELECT name, surname, email, apprenticeship FROM person WHERE role = apprentice and %s = %s
    """
    params = (field, value)
    return db.execute_query(query, params)
