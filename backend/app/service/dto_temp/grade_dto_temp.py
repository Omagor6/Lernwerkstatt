import datetime
class grade_dto_temp:
    def __init__(self, subject, grade, timestamp:datetime.datetime):
        self.subject = subject
        self.grade = str(grade)
        self.timestamp = timestamp.strftime("%d/%m/%Y, %H:%M:%S")