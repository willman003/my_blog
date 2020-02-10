from flask_wtf import FlaskForm

from wtforms import fields
from wtforms.validators import DataRequired, Length, Email

class Form_contact(FlaskForm):
    name = fields.StringField('Your name (required):',validators=[DataRequired('Your name must not be blank')])
    email = fields.StringField('Your email (required):', validators=[DataRequired('Email must not be blank')])
    subject= fields.StringField('Subject (required):')
    message = fields.TextAreaField('Your message:', validators=[DataRequired('Message must not be blank')])
    submit = fields.SubmitField('Send')