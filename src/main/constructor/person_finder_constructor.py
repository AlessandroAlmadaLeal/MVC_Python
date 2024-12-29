from src.views.person_finder_view import PersonFinderView
from src.controllers.person_finder_controller import PersonFinderController

def person_finder_constructor():

    # Instanciando um objeto da classe
    person_finder_view = PersonFinderView()
    person_finder_controller = PersonFinderController()

    person_finder_informations = person_finder_view.find_person_view()
    response = person_finder_controller.find_by_name(person_finder_informations)

    if response["success"]:
        person_finder_view.find_person_success(response["message"])
    else:
        person_finder_view.find_person_fail(response["error"])