#!/usr/bin/env python3
from flask import render_template, jsonify, request

from app import app
from app.data import DataAccess as da


@app.route('/about')
def about():
    return "This is a simple flask web app!"


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

