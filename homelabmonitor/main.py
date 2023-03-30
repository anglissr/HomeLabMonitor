from . import db
from .models import User
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort, g
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        name = current_user.username
        print(name)
    return render_template('index.html', name=name)
