from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import data_required, Length, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[data_required(), Length(min=2)])
    email = StringField('Email Address', validators=[data_required(), Email()])
    message = TextAreaField('Message', validators=[data_required()])
    send_copy = BooleanField('Send me a copy of this message')
    submit = SubmitField('Request Password Reset')
