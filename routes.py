from flask import (Blueprint, redirect, render_template, url_for)

bp = Blueprint('routes',__name__)

@bp.route('/')
def index():
    return redirect(url_for('routes.home'))

@bp.route('/home')
def home():
    return render_template('Diquesense/index.html')

@bp.route('/prevention')
def prevention():
    return render_template('Diquesense/prevention.html')

@bp.route('/about')
def about():
    return render_template('Diquesense/about.html')
