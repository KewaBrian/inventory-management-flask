from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user
from extensions import db
from models import Item

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
@login_required
def home():

    # Show only items that belong to logged-in user
    total_items = Item.query.filter_by(user_id=current_user.id).count()
    low_stock_threshold = current_app.config.get("LOW_STOCK_THRESHOLD", 5)

    total_value = (
        db.session.query(db.func.sum(Item.price * Item.quantity))
        .filter(Item.user_id == current_user.id)
        .scalar()
        or 0
    )

    low_stock = Item.query.filter(
        Item.user_id == current_user.id,
        Item.quantity < low_stock_threshold
    ).order_by(Item.quantity.asc(), Item.name.asc()).all()

    latest_items = Item.query.filter_by(
        user_id=current_user.id
    ).order_by(Item.created_at.desc()).limit(5).all()

    return render_template(
        "dashboard.html",
        total_items=total_items,
        total_value=total_value,
        low_stock=low_stock,
        low_stock_threshold=low_stock_threshold,
        latest_items=latest_items
    )
