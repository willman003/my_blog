from flask import Blueprint

main = Blueprint('main',__name__,template_folder='templates',static_folder='static')

<<<<<<< HEAD
from . import views
=======
from .views import *
>>>>>>> Complete master.html, adding main, creating DB Migration
