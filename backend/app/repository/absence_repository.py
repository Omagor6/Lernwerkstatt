import app.db.db_access_manager as db
def get_current_absences(person_id, start_time, end_time):
    query = """
    SELECT COUNT(absence_id) FROM absence WHERE personId = %s and absence_time BETWEEN %s AND %s)
    """
    params = (person_id, start_time, end_time)
    return db.fetch_query_results_as_dict(query, params)
    
