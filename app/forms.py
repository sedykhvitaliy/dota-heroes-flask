from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email


class AddNewHeroe(FlaskForm):
    name = StringField("Имя героя", validators=[InputRequired()])
    cost = IntegerField("Стоимость героя", validators=[InputRequired()])
    role = IntegerField("Роль героя", validators=[InputRequired()])
    email = EmailField("Email", validators=[Email()])
    submit = SubmitField("Добавить")
