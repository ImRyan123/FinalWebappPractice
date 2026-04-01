import os

## python -m venv .venv
from flask import Flask, render_template

def create_app(test_config=None):
    # Create and configure the Flask application
    app = Flask(__name__, instance_relative_config=True)

    # Basic configuration settings
    app.config.from_mapping(
        SECRET_KEY='dev',  # Used for session security
        DATABASE=os.path.join(app.instance_path, 'database.db'),  # Path to SQLite database file
    )

    # Load configuration depending on whether we're in testing mode or not
    if test_config is None:
        # Load the instance config file if it exists (for non-testing environments)
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Override config with test configuration if provided
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists (required for storing the database file)
    os.makedirs(app.instance_path, exist_ok=True)

    # Define a simple route for the homepage that displays blog posts
    @app.route('/')
    def index():
        from . import db
        db_conn = db.get_db()
        posts = db_conn.execute(
            'SELECT p.id, title, body, created, author_id, username'
            ' FROM post p JOIN user u ON p.author_id = u.id'
            ' ORDER BY created DESC'
        ).fetchall()
        return render_template('blog/index.html', posts=posts)
   
    # Initialize database functionality and attach it to the app
    from . import db
    db.init_app(app)

    # Import and register authentication blueprint (routes grouped in auth module)
    from . import auth
    app.register_blueprint(auth.bp)

    # Import and register blog blueprint
    from . import blog
    app.register_blueprint(blog.bp)

    # Return the configured Flask app instance
    return app