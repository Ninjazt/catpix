from flask import Flask
from importlib import import_module

from .configs import AppConfig


def create_app():
	app = Flask(__name__)
	app.config.from_object(AppConfig)
	register_router(app)
	return app

def register_router(app: Flask):
	for module_name in app.config['ROUTES']:
		module = import_module(f"app.routes.{module_name}")
		app.register_blueprint(module.blueprint)