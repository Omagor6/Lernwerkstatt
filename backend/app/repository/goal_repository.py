import app.db.db_access_manager as db
import datetime


def get_goals(person_id):
    query = """
    SELECT * FROM goal WHERE student_id = %s
    """
    params = person_id
    return db.fetch_query_results_as_dict(query, params)


def post_goal(description, due_date, goal_type, student_id):
    due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
    print(type(due_date))  # <class 'datetime.date'>
    query = """
    INSERT INTO goal (description, due_date, goal_type, student_id) VALUES (%s, %s, %s, %s);
    """
    params = (description, due_date, goal_type, student_id)
    return db.execute_query(query, params)
