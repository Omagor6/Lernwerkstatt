from app.repository import goal_repository
from datetime import timedelta
import datetime
import json


def get_goals(person_id):
    goals = goal_repository.get_goals(person_id)
    for goal in goals:
        goal["creation_date"] = goal.pop("created_timestamp").strftime("%d/%m/%Y") ##rename and assign
        goal["creation_date"] = goal["due_date"].strftime("%d/%m/%Y, %H:%M:%S") ##rename and assign
        goal["student_id"] = str(goal["student_id"])
    return goals

def post_goal(goal):
    description = goal.get("description")
    due_date = goal.get("due_date")
    goal_type = goal.get("goal_type")
    student_id = goal.get("student_id")
    print(description)
    print(due_date)
    print(goal_type)
    print(student_id)
    return goal_repository.post_goal(description, due_date, goal_type, student_id)
    