# -*- coding: utf-8 -*-


from flask import render_template, redirect, url_for
from flask.ext.login import login_required, current_user
from oleander import app, db
from oleander.forms import EmailContactForm
from oleander.models import Contact, GoogleContact, EmailContact


def email_contact_factory(email):
    if email.endswith(('gmail.com', 'googlemail.com')):
        return GoogleContact()
    return EmailContact()


@app.route('/contacts/', methods=('GET', 'POST'))
@login_required
def contacts():
    """Contacts management page."""
    form = EmailContactForm()

    if form.validate_on_submit():
        with db.transaction as session:
            contact = email_contact_factory(form.email.data)
            form.populate_obj(contact)
            contact.user = current_user
            session.add(contact)
        return redirect(url_for('contacts'))

    contacts = current_user.contacts
    return render_template('contacts.html', form=form, contacts=contacts)


@app.route('/contacts/delete/<int:id>')
@login_required
def delete_contact(id):
    """Removes contact by ID."""
    with db.transaction as session:
        Contact.query.with_polymorphic(Contact).filter(Contact.id == id).filter(Contact.user == current_user).delete()
    return redirect(url_for('contacts'))