from typing import Dict
import os

#Classe de cadastro de pessoa
class PersonRegisterView:

    #Método para registrar a pessoa - Retornando dicionário
    def register_person_view(self) -> Dict:
        #Limpando a tela
        os.system('cls||clear')
        print("Registrar Pessoa \n\n")

        name = input("Digite o nome da pessoa: ")
        age = input("Digite a idade da pessoa [Anos]: ")
        height = input("Digite a altura da pessoa [Centímetros]: ")


        new_person_informations = {
            "name": name, "age":age, "altura":height
        }

        return new_person_informations