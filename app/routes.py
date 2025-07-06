from flask import Blueprint, redirect, jsonify, abort
from app.db import SessionLocal
from app.models import Link
from sqlalchemy.orm import selectinload

bp = Blueprint('routes', __name__)

@bp.route("/")
def root():
    return jsonify({"status": "OK"})

@bp.route("/t/<slug>")
def redirect_slug(slug):
    db = SessionLocal()
    link = db.query(Link)\
        .options(selectinload(Link.versions))\
        .filter(Link.slug == slug).first()

    if not link:
        abort(404, "Link not found")

    if not link.versions:
        abort(404, "No versions found for this link")

    latest_version = link.versions[-1]  # assumes ascending order
    return redirect(latest_version.destination_url, code=302)