import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "super-secret-key-change-this"

    # SQLite Database
    DATABASE_PATH = os.path.join(BASE_DIR, "inventory.db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Pagination
    ITEMS_PER_PAGE = 6

    # Items below this quantity are shown in dashboard low-stock alerts.
    LOW_STOCK_THRESHOLD = 5
