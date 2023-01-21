from app import app
from flask import jsonify, make_response, render_template, request, redirect


@app.route("/")
def index():
    return "Dota heroes"

@app.route('/heroes_list')
def heroes_list():
    pass


@app.route('/heroe/<name>')
def heroe_list():
    pass
