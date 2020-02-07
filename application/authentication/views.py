from flask import render_template

from . import auth_bp
from .forms import *

@auth_bp.route('/login', methods =['GET','POST'])
def login():
    form_dang_nhap = Form_dang_nhap()
        

    return render_template('auth/Login.html',form_dang_nhap=form_dang_nhap)

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    form = Form_dang_ky()
    return render_template('auth/Register.html', form = form)