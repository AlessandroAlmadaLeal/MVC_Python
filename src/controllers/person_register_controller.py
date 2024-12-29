from typing import Dict

# Classe do controlador de registros
class PersonRegisterController:

    def register(self, new_person_informations: Dict) -> Dict:
        
        # Realiza a validação dos campos de dados
        try:
            # Realiza uma validação de dados da view.
            self.__validate_fields(new_person_informations)
            
            # TODO: Enviar para models para cadastro de dados 
            
            # Monta um response com as informações formatadas 
            response = self.__format_response(new_person_informations)

            # Retorna sucesso com os dados da mensagem formatados
            return { "success": True, "message": response }
        
        # Caso qualquer uma das etapas acima falhe, devolve erro.
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    # Implementando uma validação (regra de negócio).
    def __validate_fields(self, new_person_informations: Dict) -> None:
        
        # Se o nome é um campo de string
        if not isinstance(new_person_informations["name"], str):
            raise Exception ('Campo Nome incorreto!')
        
        # Se idade é um valor inteiro
        try: int(new_person_informations["idade"])
        except: raise Exception("Campo Idade incorreto!")

        # Se altura é um campo inteiro
        try: int(new_person_informations["altura"])
        except: raise Exception("Campo Altura incorreta!")

    # Método que formata os dados em um dicionário mais completo
    def __format_response(self, new_person_informations: Dict) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "attributes": new_person_informations
        }


    