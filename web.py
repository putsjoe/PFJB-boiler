
import os
from datetime import datetime

from flask import Flask, send_from_directory, redirect, abort
from flask import render_template, request, url_for, flash, g
app = Flask(__name__)

from sqlalchemy.exc import IntegrityError
from forms import EmailForm
from models import Customer


app.secret_key = 'dlskjnid89e9uc9e9feiune98n'
app.salt = 'jbjh1o83iedekjfkjf9fjen'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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
