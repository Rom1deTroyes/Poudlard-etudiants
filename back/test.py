from data import DataAccess as da
import pprint

da.connexion()

da.set_etudiant("Granger", "Hermione", 16, "Première")
da.set_etudiant("Longdubat", "Neville", 17, "Première")

pprint.pprint(da.get_etudiants())

pprint.pprint(da.get_etudiant(1))

da.deconnexion()

