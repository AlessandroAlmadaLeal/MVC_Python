from src.views.person_register_view import PersonRegisterView

def person_register_constructor():

    # Instanciando um objeto da classe
    person_register_view = PersonRegisterView()
    
    # Controller

    person_register_informations = person_register_view.register_person_view()
    # Enviar para o controller