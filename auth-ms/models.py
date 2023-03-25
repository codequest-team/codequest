import uuid

from sqlalchemy.dialects.postgresql import UUID  # type: ignore
from werkzeug.security import check_password_hash, generate_password_hash

from app import db


class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String, unique=True, nullable=False)
    nickname = db.Column(db.String, nullable=False)
    refresh_token = db.Column(db.String)
    password_hash = db.Column(db.String, nullable=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.username = self.username.lower()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User: {self.username}>"
