import app.db.db_access_manager as db

def get_goals(person_id):
    query = """
    SELECT role FROM student_mentor WHERE personId = %s
    """
    params = (person_id)
    results = db.fetch_query_results_as_dict(query, params)
    res = []
    for result in results:
        res.append(result["role"])
