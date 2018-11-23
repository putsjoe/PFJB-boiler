
import os
from datetime import datetime

from flask import Flask, send_from_directory, redirect, abort
from flask import render_template, request, url_for, flash, g

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from forms import EmailForm


app = Flask(__name__)
app.secret_key = 'dlskjnid89e9uc9e9feiune98n'
app.salt = 'jbjh1o83iedekjfkjf9fjen'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = EmailForm(request.form)
    if form.validate_on_submit():
        # Send email link
        try:
            db.session.add(Customer(email=form.email.data))
            db.session.commit()
        except IntegrityError:
            flash("This email appears to have already been registered.")
            return redirect(request.path)
        except:
            flash("An error has occured, please try again.")
            return redirect(request.path)

        # Do something with email address
        flash("Thank you for your email address")

    return render_template('index.html', form=form)


# -- DB Stuff
"""
To initiate, open a python shell and type:
    from alert import db
    db.create_all()
"""
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    confirmed = db.Column(db.Boolean(False))

    def __repr__(self):
        return '<%r>' % self.email
