from app.repository import person_repository

def get_contact_persons(person_id):
    return person_repository.get_contact_persons(person_id)

def get_students():
    students = person_repository.get_students()
    print(students)
    return students; 
