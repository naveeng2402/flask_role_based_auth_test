from sqlalchemy.sql.schema import UniqueConstraint
from .extensions import db

from flask_login import UserMixin

from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INTEGER, TEXT


class Roles(db.Model):
    id = Column(INTEGER, primary_key=True)
    role_name = Column(TEXT)

    def __repr__(self) -> str:
        return self.role_name


class User(db.Model, UserMixin):
    id = Column(INTEGER, primary_key=True)
    username = Column(TEXT)
    pwd = Column(TEXT)
    data_id = Column(INTEGER)

    roles = relationship(
        "Roles", secondary="user_roles", lazy=True, backref=backref("role", lazy=True)
    )


class UserRoles(db.Model):
    id = Column(INTEGER, primary_key=True)
    user_id = Column(
        INTEGER,
        ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"),
    )
    role_id = Column(
        INTEGER,
        ForeignKey("roles.id", ondelete="CASCADE", onupdate="CASCADE"),
    )
    __table_args__ = (UniqueConstraint("user_id", "role_id"),)


class Student(db.Model):
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT)
    mobile = Column(TEXT)


class Staff(db.Model):
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT)
    mobile = Column(TEXT)


class Admin(db.Model):
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT)
    mobile = Column(TEXT)
