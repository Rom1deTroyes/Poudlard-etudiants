import requests
import json
import os


class DataAccess :
    DATA_URL = os.environ['DATA_URL']

    @classmethod
    def connexion(cls) :
        pass

    @classmethod
    def deconnexion(cls) :
        pass

    @classmethod
    def set_etudiant(cls, nom, prenom, age, classe):
        etudiant = {"nom":nom, "prenom":prenom, "age":age, "classe":classe}
        etudiant_id = requests.post(cls.DATA_URL+'/etudiants/', etudiant)
        return str(etudiant_id.text)


    @classmethod
    def get_etudiants(cls):
        response = requests.get(cls.DATA_URL+'/etudiants/')
        etudiants = json.loads(response.content.decode("utf-8"))
        print(etudiants)
        return etudiants
    
    @classmethod
    def get_etudiant(cls, id):
        response = requests.get(cls.DATA_URL+'/etudiants/'+id)
        etudiants = json.loads(response.content.decode("utf-8"))
        print(etudiants)
        return etudiants
