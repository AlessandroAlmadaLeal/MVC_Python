from src.views.person_finder_view import PersonFinderView

def person_finder_constructor():

    # Instanciando um objeto da classe
    person_finder_view = PersonFinderView()
    
    # Controller

    person_finder_informations = person_finder_view.find_person_view()
    # Enviar para o controller