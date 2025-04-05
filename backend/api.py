from typing import Union
from app.service import person_service
from app.service.dto import goal_dto
import datetime
import json
from fastapi.responses import JSONResponse

from fastapi import FastAPI, HTTPException, status, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/contact-persons/{person_id}")
def get_contact_persons(person_id):
    return {person_service.get_contacts(person_id=person_id)}

@app.get("/students/")
def get_contacts():
    raw_rows = person_service.get_students()
    students = [dict(row) for row in raw_rows]
    return students

@app.get("/goals/{person_id}")
def get_goals(person_id: str):
    # Return a JSON response instead of using json.dumps()
    goals = [
        goal_dto.goal_dto("ABS2", "Ich kommuniziere rechtzeitig meine Absenzen", datetime.datetime(2020, 5, 17, 10, 30, 0), datetime.date(2020, 5, 17), "individual", "0"),
        goal_dto.goal_dto("AAA6", "Ich bin teamfähig", datetime.datetime(2020, 5, 17, 10, 40, 0), datetime.date(2020, 5, 20), "standard", "Erfüllt")
    ]
    return JSONResponse(content=goals)

@app.get("grades/{person_id}")
def get_grades(person_id):
    return json.dumps()