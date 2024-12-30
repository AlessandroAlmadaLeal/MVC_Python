from src.models.entities.person import Person

class __PersonRepository:
    def __init__(self) -> None:
        self.__person = []

    def registry_person(self, person) -> None:
        self.__person.append(person)

    def find_person_by_name (self, name:str) -> Person:
        for person in self.__person:
            if person.name == name: return person
        return None
    
person_repository = __PersonRepository()
