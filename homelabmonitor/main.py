from . import db
from .models import User
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort, g
from flask_login import current_user, login_required, login_manager

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    else:
        return redirect(url_for('auth.login'))


@main.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_authenticated:
        name = current_user.username
        print(name)
    return render_template('index.html', name=name)
