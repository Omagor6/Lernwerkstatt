from typing import Union
from app.service import person_service
from app.service.dto import goal_dto, grade_dto
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
    goals = [
        vars(goal_dto.goal_dto("ABS2", "Ich kommuniziere rechtzeitig meine Absenzen", datetime.datetime(2020, 5, 17, 10, 30, 0), datetime.date(2020, 5, 17), "individual", "0")),
        vars(goal_dto.goal_dto("AAA6", "Ich bin teamfähig", datetime.datetime(2026, 5, 17, 10, 40, 0), datetime.date(2026, 5, 20), "standard", "Erfüllt"))
    ]
    return JSONResponse(content=goals)

@app.get("/grades/{person_id}")
def get_grades(person_id):
    grades = [
        vars(grade_dto.grade_dto("Mathe", "4", datetime.datetime(2023, 5, 17, 10, 40, 0))),
        vars(grade_dto.grade_dto("Deutsch", "3", datetime.datetime(2022, 7, 17, 10, 20, 0))),
        vars(grade_dto.grade_dto("Deutsch", "5.5", datetime.datetime(2023, 7, 17, 10, 20, 0))),
        vars(grade_dto.grade_dto("Mathe", "6", datetime.datetime(2023, 1, 17, 10, 40, 0))),
    ]
    return JSONResponse(content=grades)