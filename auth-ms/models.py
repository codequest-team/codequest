import uuid

from sqlalchemy.dialects.postgresql import UUID  # type: ignore

from app import db


class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String, unique=True, nullable=False)
    nickname = db.Column(db.String, nullable=False)
    refresh_token = db.Column(db.String)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<User: {self.username}>"
