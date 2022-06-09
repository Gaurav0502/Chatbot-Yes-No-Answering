from crypt import methods
from flask import Flask,request, render_template, current_app as app
from flask.helpers import url_for
import flask
from entity_extractor import *
from intent_extractor import *

@app.route('/',methods=["POST"])
def respond():
    print(request.args["qs"])