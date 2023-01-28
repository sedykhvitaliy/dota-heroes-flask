from app import app, bootstrap
from flask import jsonify, make_response, render_template, request, redirect
from .models import *



@app.route("/")
def index():
    return "Dota heroes"

@app.route('/heroes_list')
def heroes_list():
    heroes = Heroes.query.all()
    return render_template('all_heroes.html', heroes=heroes, bootstrap=bootstrap)

@app.route('/heroe/<name>')
def heroe_card(name):
    heroe = Heroes.query.filter(Heroes.name==name).first()
    if heroe is not None:
        return render_template('heroe.html', heroe=heroe)
    return render_template('404.html',name=name), 404