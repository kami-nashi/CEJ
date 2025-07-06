import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Link(Base):
    __tablename__ = "links"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    versions = relationship("LinkVersion", back_populates="link", cascade="all, delete-orphan", order_by="LinkVersion.version")

class LinkVersion(Base):
    __tablename__ = "link_versions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    link_id = Column(UUID(as_uuid=True), ForeignKey("links.id", ondelete="CASCADE"), nullable=False)
    version = Column(Integer, nullable=False)
    destination_url = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    link = relationship("Link", back_populates="versions")
