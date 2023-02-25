from app import app, bootstrap, db
from flask import jsonify, make_response, render_template, request, redirect, url_for

from .forms import AddNewHeroe
from .models import *



@app.route("/")
def index():
    return render_template('main_page.html', bootstrap=bootstrap)

@app.route('/heroes_list')
def heroes_list():
    heroes = Heroes.query.all()
    return render_template('all_heroes.html', heroes=heroes, bootstrap=bootstrap)

@app.route('/heroe/<name>')
def heroe_card(name):
    heroe = Heroes.query.filter(Heroes.name==name).first()
    if heroe is not None:
        return render_template('heroe.html', heroe=heroe, stats=Stats.query.all())
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

@app.route('/heroe/heroe/edit/', methods=('GET', 'POST'))
def heroe_edit(id_heroes):
    heroe = Heroes.query.get_or_404(id_heroes)

    if request.method == 'POST':
        name = request.form['name']
        cost = request.form['cost']
        role = request.form['role']
        email = (request.form['email'])


        heroe.name = name
        heroe.cost = cost
        heroe.email = email
        heroe.role = role


        db.session.add(heroe)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('heroe_edit.html', heroe=heroe)