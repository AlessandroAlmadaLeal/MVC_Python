from typing import Dict
import os

#Classe de busca de pessoa
class PersonFinderView:

    #Método para buscar a pessoa - Retornando dicionário
    def find_person_view(self) -> Dict:
        #Limpando a tela
        os.system('cls||clear')
        print("Buscar Pessoa \n\n")
        name = input("Digite o nome da pessoa: ")

        person_finder_informations = {
            "name": name
        }

        return person_finder_informations