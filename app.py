from flask import Flask

Application = Flask("Exammer")

from main import main
from errorer import errorer
from api import api

Application.register_blueprint(errorer)
Application.register_blueprint(main)
Application.register_blueprint(api, url_prefix="/api")
