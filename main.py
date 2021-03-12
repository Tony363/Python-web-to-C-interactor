from flask import Flask, request,  render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,PasswordField
from wtforms.fields.core import BooleanField
from wtforms.fields.html5 import DateTimeField,IntegerField
from wtforms.validators import DataRequired

import os
SECRET_KEY = os.urandom(32)


import subprocess

app=Flask(__name__)
bootstrap=Bootstrap(app)


app.config['SECRET_KEY'] = SECRET_KEY


class InputForm(FlaskForm):
    first=IntegerField('',validators=[DataRequired()])
    superscript=IntegerField('',validators=[DataRequired()])
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form=InputForm()
    if form.is_submitted():
        first=form.first.data
        superscript=form.superscript.data
        process=subprocess.run(["./main",first,superscript],capture_output=True)
        string=process.CompletedProcess.stdout
        return render_template("index.html",form=form,string=string)
    else:
        return render_template("index.html",form=form)

if __name__=='__main__':
    app.run()