from flask import render_template
from flask_login import login_user, logout_user

from . import auth
from .forms import *
from ..models import *

@auth.route('/login', methods =['GET','POST'])
def login():
    thong_bao = ''
    form_dang_nhap = Form_dang_nhap()
    if form_dang_nhap.validate_on_submit():
        user = User.query.filter_by(ten_dang_nhap=form_dang_nhap.ten_dang_nhap.data).first()
        if user is not None and user.verify_password(form_dang_nhap.password.data):
            login_user(user,form_dang_nhap.remember_me.data)
            next = request.args.get('next')
            if next is None or next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        thong_bao = 'Tên đăng nhập hoặc Mật khẩu không chính xác.'

    return render_template('auth/Login.html',form_dang_nhap=form_dang_nhap, thong_bao = thong_bao)

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    form = Form_dang_ky()
    return render_template('auth/Register.html', form = form)