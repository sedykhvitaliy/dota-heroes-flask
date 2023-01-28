from app import app, db
from flask import jsonify, make_response, render_template, request, redirect
from .models import *



@app.route("/")
def index():
    return "Dota heroes"

@app.route('/heroes_list')
def heroes_list():
    heroes = Heroes.query.all()
    return render_template('all_heroes.html', heroes=heroes)

@app.route('/heroe/<name>')
def heroe_list(name):
    name = Heroes.name
    return render_template('heroe.html', name=name)
