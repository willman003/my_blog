from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired, Length, Email

from ..models import *

class Form_dang_nhap(FlaskForm):
    ten_dang_nhap = fields.StringField('Tên đăng nhập: ', validators=[DataRequired(),Length(1,64,'Nhiều hơn 64 kí tự')])
    password = fields.PasswordField('Mật khẩu', validators= [DataRequired()])
    remember_me = fields.BooleanField('Ghi nhớ ?')
    submit = fields.SubmitField('Đăng nhập')

class Form_dang_ky(FlaskForm):
    ten_dang_nhap = fields.StringField('Tên đăng nhập: ', validators=[DataRequired(),Length(1,64,'Nhiều hơn 64 kí tự')])
    password = fields.PasswordField('Mật khẩu', validators= [DataRequired()])
    email = fields.StringField('Email', validators=[DataRequired(),Email('Email không hợp lệ')])
    submit = fields.SubmitField('Đăng ký')

    def kiem_tra_ten_dang_nhap(self):
        if User.query.filter_by(ten_dang_nhap=self.ten_dang_nhap.data).first():
            return False
        return True
    
    def kiem_tra_email(self):
        if User.query.filter_by(email=self.email.data).first():
            return False
        return True
