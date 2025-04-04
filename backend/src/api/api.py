from typing import Union
from service import person_service
from service.dto import goal_dto
import datetime

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
    return [goal_dto.individual_goal_dto("Ich kommuniziere rechtzeitig meine Absenzen", datetime.datetime(2020, 5, 17, 10, 30, 0), 0), goal_dto.standard_goal_dto("Ich bin teamfähig", datetime.datetime(2020, 5, 17, 10, 40, 0), "Erfüllt")]
    return {person_service.get_goals(person_id)}


