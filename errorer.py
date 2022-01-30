"""This file act as an error handler
Error definitions defined in the
file errors.py.
Functions are transparent & explanation is not necessary
"""

from flask import render_template
from flask import Blueprint

from errors import DB

errorer = Blueprint("errorer", "Exammer")

@errorer.app_errorhandler(404)
def not_found(error):
    return render_template("errors/404.html", error=error), 404

@errorer.app_errorhandler(KeyError)
def for_keyError(error): 
    return render_template("errors/KeyError.html", error=error), 400

@errorer.app_errorhandler(DB.MultipleObjectsReturnedException)
def for_MultipleObjectsReturnedError(error):
    errorer.logger.error("MultipleObjectsReturnedException")
    return render_template("errors/MultipleObjectsReturned.html", error=error), 500

"""
import secrets
app.secret_key = secrets.token_hex()
sessions["is_logged"] = 'no'
session.pop("is_logged")
"""
# searchword = request.args.get('key', '')
