import datetime
class goal_dto:
    def __init__(self, content, due_date):
        self.content: str = content
        self.due_date: datetime = due_date
        

class individual_goal_dto(goal_dto):
    def __init__(self, rating):
        self.rating: int = rating

class standard_goal_dto(goal_dto):
    def __init__(self, rating):
        self.rating: str = rating

