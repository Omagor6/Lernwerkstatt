from repository import person_repository
def get_contact_persons(person_id):
    return person_repository.get_contact_persons(person_id)

def get_students():
    return person_repository.get_students()
