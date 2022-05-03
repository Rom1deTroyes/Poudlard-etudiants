from flask import Flask, render_template, jsonify, redirect, url_for, request
from data import DataAccess as da
import json

app = Flask(__name__)

@app.route("/")
def index():
    etudiants = da.get_etudiants()

    return render_template("index.html", etudiants=etudiants)

@app.route("/etudiant/<id>")
def get_etudiant(id):
    etudiant = da.get_etudiant(id)

    return render_template("etudiant.html", contenu=etudiant)

@app.route("/etudiant/json/<id>")
def json_etudiant(id):
    etudiant = da.get_etudiant(id)

    return jsonify(etudiant), 200

@app.route("/etudiant/inscription")
def add_etudiant():
    return render_template("inscription.html")

@app.route("/etudiant/create", methods=['POST'])
def create_etudiant():
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    age = request.form["age"]
    classe = request.form["classe"]

    rsp = da.set_etudiant(nom, prenom, age, classe)

    response = jsonify({'requests': 'okay', '_id': rsp})
    return (response)

    #return  redirect(url_for('index'), code=302)

if __name__ == "__main__" :
    app.run(debug=True, port=8080)
