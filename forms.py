
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import BooleanField, StringField, SubmitField
from wtforms import validators


class EmailForm(FlaskForm):
    email = StringField('Email Address',
        [validators.Length(min=6, max=35),
        validators.InputRequired("Please enter your email address.")]
    )
    accept_tos = BooleanField('I accept the Agreement', [validators.DataRequired()])
    submit = SubmitField('Submit')
