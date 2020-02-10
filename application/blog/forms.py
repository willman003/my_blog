from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired

class Form_post(FlaskForm):
    title = fields.StringField('Tiêu đề:', validators=[DataRequired()])
    feeling = fields.SelectField('Cảm xúc:', choices=[('sad','Buồn'),('happy','Hạnh phúc'),('angry','Giận'),('hope','Hi vọng'),('idea','Ý tưởng'),('heart','Yêu thương')])
    text = fields.TextAreaField('Nội dung:')
    submit = fields.SubmitField('Gửi')

    
