from repository import person_repository
def get_persons(person_id):
    if person_id == person_id: ## TODO hier checken ob person lehrling oder nicht
        return person_repository.get_contact_persons(person_id)
    else:
        return person_repository.get_students()
