from app import app, bootstrap, db
from flask import jsonify, make_response, render_template, request, redirect, url_for

from .forms import AddNewHeroe, HeroeCard
from .models import *



@app.route("/")
def index():
    return render_template('main_page.html', bootstrap=bootstrap)

@app.route('/heroes_list')
def heroes_list():
    heroes = Heroes.query.all()
    return render_template('all_heroes.html', heroes=heroes, bootstrap=bootstrap)

@app.route('/heroe/<name>', methods=['GET', 'POST'])
def heroe_card(name):
    heroe = Heroes.query.filter(Heroes.name==name).first()
    if heroe is not None:
        form = HeroeCard(obj=heroe)
        if request.method == 'POST':
            print('post')
        return render_template('heroe.html', form=form, heroe=heroe)
    return render_template('404.html',name=name), 404

@app.route('/heroe/new', methods=['GET', 'POST'])
def heroe_add():
    form = AddNewHeroe()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form.get("name")
            cost = request.form.get("cost")
            role = request.form.get("role")
            email = request.form.get("email")
            heroe = Heroes(name=name, cost=cost, role=role)
            db.session.add(heroe)
            db.session.commit()
            print('Добавлен новый герой пользователем: ', email)
            return redirect('/')
    return render_template('heroe_add.html',form=form)

@app.route('/heroe/edit/<id_heroes>', methods=('GET', 'POST'))
def heroe_edit(id_heroes):
    heroe = Heroes.query.get_or_404(id_heroes)

    if request.method == 'POST':
        print('heroe_edit', id_heroes)

@app.route('/heroe/delete/<id_heroes>', methods=('GET', 'POST'))
def heroe_delete(id_heroes):
    heroe = Heroes.query.get_or_404(id_heroes)

    if request.method == 'POST':
        print('heroe_delete', id_heroes)