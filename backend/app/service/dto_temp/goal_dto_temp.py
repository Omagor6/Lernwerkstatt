import datetime
class goal_dto_temp:
    def __init__(self, goal_id, description,creation_date: datetime.date, due_date: datetime.datetime, goal_type, grading):
        self.goal_id: str = goal_id
        self.description: str = description
        self.creation_date: str = creation_date.strftime("%d/%m/%Y")
        self.due_date: str = due_date.strftime("%d/%m/%Y, %H:%M:%S")
        self.goal_type: str = goal_type
        self.grading: str = str(grading)

