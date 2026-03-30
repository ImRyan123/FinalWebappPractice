import sqlite3
from datetime import datetime

import click
from flask import current_app, g


def get_db():
    # Check if a database connection already exists in the application context
    if 'db' not in g:
        # Create a new connection to the database defined in app config
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Return rows as dictionary-like objects instead of tuples
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    # Remove the database connection from the app context if it exists
    db = g.pop('db', None)

    # Close the connection if it was created
    if db is not None:
        db.close()


def init_db():
    # Get database connection
    db = get_db()

    # Open and execute SQL schema file to create tables
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    # Initialize the database schema
    init_db()
    # Print confirmation message to the CLI
    click.echo('Initialized the database.')


# Register a converter so SQLite can properly parse timestamp fields into Python datetime objects
sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)


def init_app(app):
    # Register function to run when the app context tears down (cleanup DB connection)
    app.teardown_appcontext(close_db)

    # Register custom CLI command: flask init-db
    app.cli.add_command(init_db_command)