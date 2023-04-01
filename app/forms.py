from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired, EqualTo


class AddNewHeroe(FlaskForm):
    name = StringField("Имя героя", validators=[InputRequired()])
    cost = IntegerField("Стоимость героя", validators=[InputRequired()])
    role = IntegerField("Роль героя", validators=[InputRequired()])
    email = EmailField("Email", validators=[Email()])
    submit = SubmitField("Добавить")

class HeroeCard(FlaskForm):
    name = StringField("Имя героя", validators=[InputRequired()])
    cost = IntegerField("Стоимость героя", validators=[InputRequired()])
    role = IntegerField("Роль героя", validators=[InputRequired()])

class LoginForm(FlaskForm):
    email =EmailField("Почта", validators=[InputRequired(), DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[InputRequired(), DataRequired()])
    submit = SubmitField("Авторизоваться")

class RegistrationForm(FlaskForm):
    email = EmailField("Почта", validators=[InputRequired(), DataRequired(), Email()])
    password = PasswordField("Введите пароль", validators=[InputRequired(), DataRequired(),
                                                        EqualTo('password_confirm', message='Пароли не совпадают')])
    password_confirm = PasswordField("Подтвердите пароль", validators=[InputRequired(), DataRequired(),
                                                                       EqualTo('password',
                                                                               message='Пароли не совпадают')])
    submit = SubmitField("Зарегестрироваться")