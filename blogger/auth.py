import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from blogger.db import get_db

# Create a Blueprint for authentication routes
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    # Handle form submission (POST) or display form (GET)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        # Basic validation checks
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        # If no validation errors, attempt to insert new user
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                # Triggered if username already exists (unique constraint)
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        # Display error message to user
        flash(error)

    # Render registration template for GET requests (or after errors)
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    # Handle login form submission
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        # Fetch user record from database
        # FIX: include 'id' in SELECT since it is used later
        user = db.execute(
            'SELECT id, username, password FROM user WHERE username = ?', (username,)
        ).fetchone()

        # Validate username and password
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        # If authentication succeeds, store user in session
        if error is None:
            session.clear()
            session['user_id'] = user['id']  # FIX: now valid since id is selected
            return redirect(url_for('index'))

        # Show login error
        flash(error)

    # Render login template for GET requests (or after errors)
    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    # Runs before every request to load the current logged-in user into 'g'
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        # Fetch full user record using stored session user_id
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


def login_required(view):
    # Decorator to restrict access to authenticated users only
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            # Redirect unauthenticated users to login page
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.route('/logout')
def logout():
    # Clear session to log the user out
    session.clear()
    return redirect(url_for('index'))