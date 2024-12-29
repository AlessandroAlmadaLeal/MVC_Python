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
    
    def find_person_success(self, message: Dict) -> None:
        os.system('cls||clear')
        success_message = f'''
            Usuário encontrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"]}
            Informações:
                Name: { message["Informações"]["name"]}
        '''
        print(success_message)

    def find_person_fail(self, error: str) -> None:
        os.system('cls|| clear')
        fail_message=f'''
            Falha ao encontrar usuário!

            Erro: {error}

        '''
        print(fail_message)

