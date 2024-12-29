from .constructor.introduction_process import introduction_process
from .constructor.person_finder_constructor import person_finder_constructor
from .constructor.person_register_constructor import person_register_constructor

def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': person_register_constructor()
        elif command == '2': person_finder_constructor()
        elif command == '5': exit()
        else: print ("\n Comando não encontrado\n\n")