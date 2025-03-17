from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify)

bp = Blueprint('home',__name__,url_prefix='/home')

@bp.route("/")
def homePage():
    return "Hello World"
