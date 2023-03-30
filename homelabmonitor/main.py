from . import db
from .models import User
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort, g
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('index.html')
