from typing import Union
from app.service import person_service
from app.service.dto_temp import goal_dto_temp, grade_dto_temp
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

@app.get("/person/contact-persons/{person_id}")
def get_contact_persons(person_id):
    return {person_service.get_contacts(person_id=person_id)}

@app.get("/person/students/")
def get_contacts():
    raw_rows = person_service.get_students()
    students = [dict(row) for row in raw_rows]
    return students

@app.get("/person/students/radar-chart/{person_id}")
def get_radar_chart_data(person_id: str):
    return person_service.get_radar_chart_info(person_id)

@app.get("/goals/{person_id}")
def get_goals(person_id: str):
    goals = goal_serviceget_goals(person_id)
    ###DUMMY###
    goals = [
        vars(goal_dto_temp.goal_dto_temp("ABS2", "Ich kommuniziere rechtzeitig meine Absenzen", datetime.datetime(2020, 5, 17, 10, 30, 0), datetime.date(2020, 5, 17), "individual", "0")),
        vars(goal_dto_temp.goal_dto_temp("AAA6", "Ich bin nehme aktiv an diskussionen teil", datetime.datetime(2026, 5, 17, 10, 40, 0), datetime.date(2026, 5, 20), "standard", "Erfüllt"))
    ]
    ###DUMMY###
    return JSONResponse(content=goals)

@app.get("/subjects/grades/{person_id}")
def get_grades(person_id):
    ###DUMMY###
    grades = [
        vars(grade_dto_temp.grade_dto_temp("Mathe", "6", datetime.datetime(2023, 5, 17, 10, 40, 0))),
        vars(grade_dto_temp.grade_dto_temp("Deutsch", "3", datetime.datetime(2022, 7, 17, 10, 20, 0)))
    ]
    ###DUMMY###
    return JSONResponse(content=grades)