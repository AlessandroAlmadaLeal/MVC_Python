from src.views.person_register_view import PersonRegisterView
from src.controllers.person_register_controller import PersonRegisterController

def person_register_constructor():

    # Instanciando um objeto das classes
    person_register_view = PersonRegisterView()
    person_register_controller = PersonRegisterController()

    # Invocando os métodos das classes
    person_register_informations = person_register_view.register_person_view()
    response = person_register_controller.register(person_register_informations)

    # Acionando as páginas conforme o cenário de registro
    if response["success"]:
        person_register_view.registry_person_success(response["message"])
    else:
        person_register_view.registry_person_fail(response["error"])