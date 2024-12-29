from .constructor.introduction_process import introduction_process

def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': print('\n Comando 1 foi acionado!\n\n')
        elif command == '2': print ('\n Comando 2 foi acionado!\n\n')
        elif command == '5': exit()
        else: print ("\n Comando não encontrado\n\n")