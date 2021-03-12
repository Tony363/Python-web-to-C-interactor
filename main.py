from flask import Flask, request,  render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,PasswordField
from wtforms.fields.core import BooleanField
from wtforms.fields.html5 import DateTimeField,IntegerField
from wtforms.validators import DataRequired
app=Flask(__name__)
bootstrap=Bootstrap(app)

class InputForm(FlaskForm):
    first=IntegerField('',validators=[DataRequired()])
    superscript=IntegerField('',validators=[DataRequired()])
    submit=SubmitField('Submit')

