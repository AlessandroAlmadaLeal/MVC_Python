from typing import Dict
import os

class PersonFinderController:
    def find_by_name(self, person_finder_informations: Dict) -> Dict:
        try:
            self.__validate_fields(person_finder_informations)

            #TODO: person = Buscar no banco de dados

            response = self.__format_response(None)
            return {"success": True, "message": response}

        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __validate_fields(self, person_finder_informations: Dict) -> None:
        if not isinstance(person_finder_informations["name"], str):
            raise Exception('Campo Nome inválido!')
        
    def __format_response(self, person: any) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "Informações":{
                "name": "nome teste"
            }
        }