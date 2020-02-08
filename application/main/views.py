<<<<<<< HEAD
from . import main_bp
=======
from flask import render_template, redirect, url_for
from flask_login import login_required

from . import main

@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')
>>>>>>> Complete master.html, adding main, creating DB Migration
