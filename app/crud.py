from sqlalchemy.orm import Session
from .models import Link, Click
from .utils import generate_slug
import uuid

def create_link(db: Session, destination_url: str):
    slug = generate_slug()
    link = Link(id=uuid.uuid4(), slug=slug, destination_url=destination_url)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link

def get_link_by_slug(db: Session, slug: str):
    return db.query(Link).filter(Link.slug == slug).first()

def log_click(db: Session, link_id, ip, referrer, user_agent):
    click = Click(
        id=uuid.uuid4(),
        link_id=link_id,
        ip_address=ip,
        referrer=referrer,
        user_agent=user_agent
    )
    db.add(click)
    db.commit()
