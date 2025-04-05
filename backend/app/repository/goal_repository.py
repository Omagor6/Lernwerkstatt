import app.db.db_access_manager as db

def get_goals(person_id):
    query = """
    SELECT * FROM goals WHERE student_id = %s
    """
    params = (person_id)
    return db.fetch_query_results_as_dict(query, params)

