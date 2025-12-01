import os
from flask import Flask
from config import Config
from extensions import db, login_manager
import pytz
from main import bp as main_bp
from auth import bp as auth_bp
from dashboard import dashboard as dashboard_bp
from profile import profile as profile_bp


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Load config
    app.config.from_object(Config)

    # Make pytz available in Jinja templates
    app.jinja_env.globals['pytz'] = pytz

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(profile_bp, url_prefix="/profile")

    # Create database on first run
    with app.app_context():
        if not os.path.exists(app.config["DATABASE_PATH"]):
            db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
import os
from flask import Flask
from config import Config
from extensions import db, login_manager
import pytz

def create_app(test_config=None):
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Load config
    if test_config:
        # When tests run, pytest will send {'TESTING': True}
        app.config.from_object(Config)
        app.config.update(test_config)
    else:
        app.config.from_object(Config)

    # Make pytz available in Jinja templates
    app.jinja_env.globals['pytz'] = pytz

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from main import bp as main_bp
    from auth import bp as auth_bp
    from dashboard import dashboard as dashboard_bp
    from profile import profile as profile_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(profile_bp, url_prefix="/profile")

    # Create database (ONLY in production, not in tests)
    if not test_config:
        with app.app_context():
            if not os.path.exists(app.config["DATABASE_PATH"]):
                db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
