from flask import Blueprint


#Khởi tạo Blueprint
auth_bp = Blueprint('auth_bp',__name__,template_folder='templates',static_folder='static')

from . import views