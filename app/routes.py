import os

from werkzeug.utils import secure_filename

from app import app, bootstrap, db
from flask import jsonify, make_response, render_template, request, redirect, url_for, flash

from .forms import AddNewHeroe, HeroeCard
from .models import *



@app.route("/")
def index():
    return render_template('main_page.html', bootstrap=bootstrap)

@app.route('/heroes_list')
def heroes_list(alert=None):
    heroes = Heroes.query.all()
    return render_template('all_heroes.html', heroes=heroes, bootstrap=bootstrap, alert=alert)

@app.route('/heroe/<name>', methods=['GET', 'POST'])
def heroe_card(name):
    heroe = Heroes.query.filter(Heroes.name==name).first()
    if heroe is not None:
        form = HeroeCard(obj=heroe)
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                return redirect(request.url)

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
            return heroes_list('success')
    return render_template('heroe_add.html',form=form)

@app.route('/heroe/edit/<id_heroes>', methods=('GET', 'POST'))
def heroe_edit(id_heroes):
    heroe = Heroes.query.get_or_404(id_heroes)
    form = HeroeCard()
    if request.method == 'POST':
        heroe.cost = request.form.get("cost")
        heroe.role = request.form.get("role")
        db.session.commit()
        return render_template('heroe.html', id_heroes=id_heroes, form=form, heroe=heroe)

    return render_template('heroe.html', heroe=heroe)

@app.route('/heroe/delete/<id_heroes>', methods=('GET', 'POST'))
def heroe_delete(id_heroes):
    heroe = Heroes.query.get_or_404(id_heroes)
    if request.method == 'POST':
        db.session.delete(heroe)
        db.session.commit()
        return heroes_list('danger')
    else:
        return render_template('heroe.html', heroe=heroe)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
