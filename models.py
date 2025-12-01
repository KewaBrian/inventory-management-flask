from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from extensions import db, login_manager
import pytz

# -----------------------------
# USER MODEL
# -----------------------------
class User(UserMixin, db.Model):
    created_at = db.Column(db.DateTime, default=lambda: datetime.utcnow())
    last_login = db.Column(db.DateTime, default=None)
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    email = db.Column(db.String(120), unique=True)
    bio = db.Column(db.String(300))

    # avatar filename (default avatar included in static folder)
    avatar = db.Column(db.String(120), default="default.png")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Constructor helpers
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -----------------------------
# ITEM MODEL
# -----------------------------
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, default=0.0)

    # NEW: category and image filename
    category = db.Column(db.String(80), nullable=True)         # e.g. "electronics"
    image_filename = db.Column(db.String(200), nullable=True)  # store filename under static/uploads/

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # optional: link item → user who added it
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', backref='items')
