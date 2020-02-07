from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired, Length, Email

class Form_dang_nhap(FlaskForm):
    ten_dang_nhap = fields.StringField('Tên đăng nhập: ', validators=[DataRequired,Length(1,64,'Nhiều hơn 64 kí tự')])
    password = fields.PasswordField('Mật khẩu', validators= [DataRequired()])
    remember_me = fields.BooleanField('Ghi nhớ ?')
    submit = fields.SubmitField('Đăng nhập')

class Form_dang_ky(FlaskForm):
    ten_dang_nhap = fields.StringField('Tên đăng nhập: ', validators=[DataRequired,Length(1,64,'Nhiều hơn 64 kí tự')])
    password = fields.PasswordField('Mật khẩu', validators= [DataRequired()])
    email = fields.StringField('Email', validators=[Email('Email không hợp lệ')])
    submit = fields.SubmitField('Đăng ký')
