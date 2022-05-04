#!/usr/bin/env python3
from flask import render_template, jsonify, request
from app.data import DataAccess as da
from app import app


@app.route('/about')
def about():
    return "This is a simple flask web app!"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/etudiants/<id>")
def get_etudiant(id):
    etudiant = da.get_etudiant(id)
    return jsonify(etudiant), 200


@app.route("/etudiants/", methods=['GET'])
def get_etudiants():
    etudiants = da.get_etudiants()
    return jsonify(etudiants), 200


@app.route("/etudiants/", methods=['POST'])
def create_etudiant():
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    age = request.form["age"]
    classe = request.form["classe"]

    rsp = da.set_etudiant(nom, prenom, age, classe)

    response = jsonify({'requests': 'okay', '_id': rsp})
    return (response)
