from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Global extensions (used by blueprints)
db = SQLAlchemy()
login_manager = LoginManager()

# Where users get redirected when not logged in
login_manager.login_view = "auth.login"
login_manager.login_message_category = "warning"
