from app.repository import goal_repository
from datetime import timedelta
import datetime
import json


def get_goals(person_id):
    return goal_repository.get_goals(person_id)
    