from flask import Blueprint


#Khởi tạo Blueprint
auth = Blueprint('auth',__name__,template_folder='templates',static_folder='static')

from . import views