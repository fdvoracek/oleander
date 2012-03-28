# -*- coding: utf-8 -*-


from flask.ext import wtf
from models import tz_choices


class Form(wtf.Form):
    """Oleander base form class."""

    def add_error(self, field_name, error):
        """Adds error message."""
        if field_name in self.errors:
            self.errors[field_name].append(error)
        else:
            self.errors[field_name] = [error]


class SignUpForm(Form):
    """Sign up form."""

    name = wtf.TextField('Name', validators=[
        wtf.Required(),
        wtf.Length(max=100),
    ])
    email = wtf.TextField('E-mail', validators=[
        wtf.Required(),
        wtf.Email(),
        wtf.Length(max=100),
    ])
    password = wtf.PasswordField('Password', validators=[
        wtf.Required(),
    ])
    password_check = wtf.PasswordField('Password once more', validators=[
        wtf.EqualTo('password', message='Passwords must match'),
    ])


class SignInForm(Form):
    """Sign in form."""

    email = wtf.TextField('E-mail', validators=[
        wtf.Required(),
        wtf.Length(max=100),
    ])
    password = wtf.PasswordField('Password', validators=[
        wtf.Required(),
    ])


class SettingsForm(Form):
    """Simple settings form."""

    name = wtf.TextField('Name', validators=[
        wtf.Required(),
        wtf.Length(max=100),
    ])
    email = wtf.TextField('E-mail', validators=[
        wtf.Required(),
        wtf.Email(),
        wtf.Length(max=100),
    ])
    # password = wtf.PasswordField('New password', validators=[
    #     wtf.Required(),
    # ])
    # password_check = wtf.PasswordField('Password once more', validators=[
    #     wtf.EqualTo('password', message='Passwords must match'),
    # ])
    timezone = wtf.SelectField('My timezone is', choices=tz_choices(), validators=[
        wtf.Required(),
    ])
