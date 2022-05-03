from pymongo import MongoClient

class DataAccess :
    user = "root"
    mdp = "pass12345"
    db_name = "ecole"
    collection_name = "etudiants"

    @classmethod
    def connexion(cls) :
        cls.client = MongoClient(f"mongodb://{cls.user}:{cls.mdp}@127.0.0.1:27018")

        cls.db = cls.client[cls.db_name]
        cls.etudiants = cls.db[cls.collection_name]

    @classmethod
    def deconnexion(cls) :
        cls.client.close()

    @classmethod
    def set_etudiant(cls, nom, prenom, age, classe):
        taille = cls.etudiants.count_documents({})
        taille = taille+1
        
        etudiant = {"_id":taille, "nom":nom, "prenom":prenom, "age":age, "classe":classe}
        cls.etudiants.insert_one(etudiant)

    @classmethod
    def get_etudiants(cls):
        etudiants = cls.etudiants.find({})
        return list(etudiants)
    
    @classmethod
    def get_etudiant(cls, id):
        etudiant = cls.etudiants.find_one({"_id":id})
        return etudiant
