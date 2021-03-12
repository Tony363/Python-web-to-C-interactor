from flask import Flask, request,  render_template, url_for, redirect
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap=Bootstrap(app)

