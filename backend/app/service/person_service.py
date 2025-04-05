from app.repository import person_repository, subject_repository, absence_repository
from datetime import timedelta
import datetime
import json

def get_contact_persons(person_id):
    return person_repository.get_contact_persons(person_id)

def get_students():
    students = person_repository.get_students()
    return students; 

def get_radar_chart_info(person_id):
    last_monday = get_last_monday()

    subjects = subject_repository.get_current_subjects(person_id)
    absences = absence_repository.get_absences(person_id, last_monday.strftime('%Y-%m-%d %H:%M:%S'), datetime.now().strftime('%Y-%m-%d %H:%M:%S')) ###strftime Format depends on DB setup

    ### Grade Calculations
    total_value = 0
    for subject in subjects:
        grade = json.loads(subject["grade"])
        score = grade["grade"]
        weight = grade["weight"]
        ### CLASSIFY BY SUBJECT-BLOCK HERE ###
        total_value += score*grade
    avg_grade = total_value%len(subjects)


    ### Absence Quota Calculation
    timediff = datetime.now() - last_monday
    absence_quota = absences / int(timediff.days)

    return {"grade": avg_grade, "presence": (1-absence_quota)*100}
    



def get_last_monday():
    base_date = datetime.now()
    monday =  base_date - timedelta(days=base_date.isoweekday() - 1)
    print(monday)