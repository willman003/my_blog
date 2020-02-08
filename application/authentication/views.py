<<<<<<< HEAD
from flask import render_template
=======
from flask import render_template, redirect, url_for, request
>>>>>>> Complete master.html, adding main, creating DB Migration
from flask_login import login_user, logout_user

from . import auth
from .forms import *
from ..models import *

@auth.route('/login', methods =['GET','POST'])
def login():
    thong_bao = ''
    form_dang_nhap = Form_dang_nhap()
<<<<<<< HEAD
    if form_dang_nhap.validate_on_submit():
        user = User.query.filter_by(ten_dang_nhap=form_dang_nhap.ten_dang_nhap.data).first()
        if user is not None and user.verify_password(form_dang_nhap.password.data):
            login_user(user,form_dang_nhap.remember_me.data)
=======
    thong_bao = ''
    if form_dang_nhap.validate_on_submit():
        user = User.query.filter_by(ten_dang_nhap=form_dang_nhap.ten_dang_nhap.data).first()
        if user is not None and user.verify_password(form_dang_nhap.password.data):
            login_user(user, form_dang_nhap.remember_me.data)
>>>>>>> Complete master.html, adding main, creating DB Migration
            next = request.args.get('next')
            if next is None or next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
<<<<<<< HEAD
        thong_bao = 'Tên đăng nhập hoặc Mật khẩu không chính xác.'
=======
        thong_bao = 'Tên đăng nhập hoặc Mật khẩu không hợp lệ.'
>>>>>>> Complete master.html, adding main, creating DB Migration

    return render_template('auth/Login.html',form_dang_nhap=form_dang_nhap, thong_bao = thong_bao)

@auth.route('/register',methods=['GET','POST'])
def register():
    form = Form_dang_ky()
    return render_template('auth/Register.html', form = form)

@auth.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))