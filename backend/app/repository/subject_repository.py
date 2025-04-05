import app.db.db_access_manager as db
def get_current_subjects(person_id):
    query = """
    SELECT name, grade FROM subject WHERE personId = %s and semester = (SELECT MAX(semester) FROM subject group by semester)
    """
    params = (person_id)
    return db.fetch_query_results_as_dict(query, params)
