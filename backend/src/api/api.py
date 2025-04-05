from typing import Union
from service import person_service
from service.dto import goal_dto
import datetime
import json

from fastapi import FastAPI

app = FastAPI()

@app.get("/contact-persons/{person_id}")
def get_contact_persons(person_id):
    return {person_service.get_contacts(person_id=person_id)}

@app.get("/students/")
def get_contacts():
    return {person_service.get_students()}

@app.get("/goals/{person_id}")
def get_goals(person_id):
    return json.dumps(goal_dto.goal_dto("ABS2", "Ich kommuniziere rechtzeitig meine Absenzen", datetime.datetime(2020, 5, 17, 10, 30, 0), datetime.date(2020, 5, 17), "individual", "0"), goal_dto.goal_dto("AAA6", "Ich bin teamfähig", datetime.datetime(2020, 5, 17, 10, 40, 0), datetime.date(2020, 5, 20), "standard", "Erfüllt"))
    return {person_service.get_goals(person_id)}

@app.get("grades/{person_id}")
def get_grades(person_id):
    return json.dumps()


