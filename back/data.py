from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient


class DataAccess :
    user = "root"
    mdp = "root"
    db_name = "ecole"
    collection_name = "etudiants"

    @classmethod
    def connexion(cls) :
        cls.client = MongoClient(f"mongodb://{cls.user}:{cls.mdp}@127.0.0.1:27017")

        cls.db = cls.client[cls.db_name]
        cls.etudiants = cls.db[cls.collection_name]

    @classmethod
    def deconnexion(cls) :
        cls.client.close()

    @classmethod
    def set_etudiant(cls, nom, prenom, age, classe):
        cls.connexion()
        etudiant = {"nom":nom, "prenom":prenom, "age":age, "classe":classe}
        etudiant_id = cls.etudiants.insert_one(etudiant).inserted_id
        cls.deconnexion()
        return str(etudiant_id)


    @classmethod
    def get_etudiants(cls):
        cls.connexion()
        etudiants = list(cls.etudiants.find({}))
        cls.deconnexion()
        return etudiants
    
    @classmethod
    def get_etudiant(cls, id):
        cls.connexion()
        #etudiant = cls.etudiants.find_one({"_id":id})
        etudiant = cls.etudiants.find_one({'_id': ObjectId(id)})
        cls.deconnexion()
        etudiant['_id'] = str(etudiant['_id'])
        return etudiant
