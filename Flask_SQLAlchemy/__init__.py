# To create a package we need to have a directory with our package name 
# that includes a __init__.py.  This is used as a placeholder for
# the src.  The __init__.py files are required to make Python treat the 
# directories as containing packages; this is done to prevent directories 
# with a common name, such as string, from unintentionally hiding valid 
# modules that occur later on the module search path.

import os

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash

def app(test_config=None):
    # Initial setup omitted

    from .models import db, User

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/sign_up', methods=('GET', 'POST'))
    def sign_up():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            error = None

            if not username:
                error = 'Username is required.'
            elif not password:
                error = 'Password is required.'
            elif User.query.filter_by(username=username).first():
                error = 'Username is already taken.'

            if error is None:
                user = User(username=username, password=password)
                db.session.add(user)
                db.session.commit()
                flash("Successfully signed up! Please log in.", 'success')
                return redirect(url_for('log_in'))

            flash(error, 'error')

        return render_template('sign_up.html')

    @app.route('/log_in')
    def log_in():
        return "Login"

    return app