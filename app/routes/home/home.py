from flask import Blueprint, render_template, session, request

blueprint = Blueprint("home", __name__, url_prefix="/")

@blueprint.route('/')
def home():
	return render_template("index.html")

@blueprint.route('/obrigado')
def thanks():
	return render_template("thanks.html")