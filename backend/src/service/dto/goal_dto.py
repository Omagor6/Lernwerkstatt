import datetime
class goal_dto:
    def __init__(self, goal_id, description,creation_date, due_date, goal_type):
        self.goal_id: str = goal_id
        self.description: str = description
        self.creation_date: datetime.date = creation_date
        self.due_date: datetime.datetime = due_date
        self.goal_tpye: str = goal_type
        

class individual_goal_dto(goal_dto):
    def __init__(self, grading):
        self.grading: int = grading

class standard_goal_dto(goal_dto):
    def __init__(self, grading):
        self.grading: str = grading

