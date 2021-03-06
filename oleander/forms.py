# -*- coding: utf-8 -*-


from flask.ext import wtf
from pytz import common_timezones
import times


def tz_choices():
    """Prepares timezone choices for use in forms."""
    choices = []
    for tz in common_timezones:
        places = tz.split('/')
        places.reverse()
        label = ', '.join(places).replace('_', ' ')
        time = times.format(times.now(), tz, '%H:%M')
        choices.append((tz, time + u' – ' + label))

    return sorted(choices, key=lambda choice: choice[1])


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
    ], description='e.g. Johnny')
    primary_email = wtf.TextField('E-mail', validators=[
        wtf.Required(),
        wtf.Email(),
        wtf.Length(max=100),
    ])
    password = wtf.PasswordField('Password', validators=[
        wtf.Required(),
    ])
    password_check = wtf.PasswordField('Password once more', validators=[
        wtf.EqualTo('password', message='Passwords must match'),
    ], description='protection against typos')


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
    ], description='e.g. Johnny')
    email = wtf.TextField('E-mail', validators=[
        wtf.Required(),
        wtf.Email(),
        wtf.Length(max=100),
    ])
    timezone = wtf.SelectField('My timezone is', choices=tz_choices(), validators=[
        wtf.Required(),
    ])


class PasswordForm(Form):
    """Password changing form."""

    old_password = wtf.PasswordField('Old password', validators=[
        wtf.Required(),
    ])
    new_password = wtf.PasswordField('New password', validators=[
        wtf.Required(),
    ])
    password_check = wtf.PasswordField('New password once more', validators=[
        wtf.EqualTo('new_password', message='Passwords must match'),
    ], description='protection against typos')


class EmailContactForm(Form):
    """Basic email contact creation form."""

    name = wtf.TextField('Name', validators=[
        wtf.Required(),
        wtf.Length(max=100),
    ], description='e.g. Susan')
    email = wtf.TextField('E-mail', validators=[
        wtf.Required(),
        wtf.Email(),
        wtf.Length(max=100),
    ])


class EventForm(Form):
    """Form to create or edit an event."""

    name = wtf.TextField('Name', validators=[
        wtf.Required(),
        wtf.Length(max=200),
    ])
    starts_at = wtf.DateTimeField('When', format='%Y-%m-%d %H:%M')
    venue = wtf.TextField('Where', validators=[
        wtf.Length(max=200),
    ])
    description = wtf.TextAreaField('What')
    contacts_invited_ids_str = wtf.HiddenField()

