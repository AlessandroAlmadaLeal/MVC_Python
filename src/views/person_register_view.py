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
        age = input("Digite a idade da pessoa: ")
        height = input("Digite a altura da pessoa: ")

        new_person_informations = {
            "name": name, "idade":age, "altura":height
        }      

        return new_person_informations

    # Em caso de sucesso essa página será retornada
    def registry_person_success(self, message: Dict) -> None:
        os.system('cls||clear')
                
        success_message = f''' 
            Usuário cadastrado com sucesso!
            
            Tipo: { message["type"] }
            Registros: { message["count"] }
            Informações:
                Nome: { message["attributes"]["name"] }
                Idade: { message["attributes"]["idade"] }
        '''
        print(success_message)

    # Em caso de falha essa página será retornada
    def registry_person_fail(self, error: str) -> None:
        os.system('cls||clear')
        fail_messege = f'''
            Falha ao cadastrar usuário!

            Erro: { error }
        '''
        print(fail_messege)