from flask import Flask, render_template, jsonify, redirect, url_for, request
from data import DataAccess as da
import json

app = Flask(__name__)

@app.route("/")
def index():
    da.connexion()
    etudiants = da.get_etudiants()
    da.deconnexion()

    return render_template("index.html", etudiants=etudiants)

@app.route("/etudiant/<int:id>")
def get_etudiant(id):
    da.connexion()
    etudiant = da.get_etudiant(id)
    da.deconnexion()

    return render_template("etudiant.html", contenu=etudiant)

@app.route("/etudiant/json/<int:id>")
def json_etudiant(id):
    da.connexion()
    etudiant = da.get_etudiant(id)
    da.deconnexion()

    return jsonify(etudiant), 200

if __name__ == "__main__" :
    app.run(debug=True)