from .extensions import db

from flask_login import UserMixin

from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import Column, ForeignKey, UniqueConstraint
from sqlalchemy.types import INTEGER, TEXT


class Roles(db.Model):
    query: db.Query

    id = Column(INTEGER, primary_key=True)
    role_name = Column(TEXT)

    def __init__(self, role_name: str) -> None:
        self.role_name = role_name

    def __repr__(self) -> str:
        return self.role_name


class User(db.Model, UserMixin):
    query: db.Query

    id = Column(INTEGER, primary_key=True)
    username = Column(TEXT)
    pwd = Column(TEXT)
    data_id = Column(INTEGER)

    roles = relationship(
        "Roles", secondary="user_roles", lazy=True, backref=backref("role", lazy=True)
    )

    def __init__(self, username: str, pwd: str, data_id: int):
        self.username, self.pwd, self.data_id = username, pwd, data_id


class UserRoles(db.Model):
    query: db.Query

    id = Column(INTEGER, primary_key=True)
    user_id = Column(
        INTEGER, ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    role_id = Column(
        INTEGER, ForeignKey("roles.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    __table_args__ = (UniqueConstraint("user_id", "role_id"),)


class Student(db.Model):
    query: db.Query

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT)
    mobile = Column(TEXT)

    def __init__(self, name: str, mobile: str):
        self.name, self.mobile = name, mobile


class Staff(db.Model):
    query: db.Query

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT)
    mobile = Column(TEXT)

    def __init__(self, name: str, mobile: str):
        self.name, self.mobile = name, mobile


class Admin(db.Model):
    query: db.Query

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT)
    mobile = Column(TEXT)

    def __init__(self, name: str, mobile: str):
        self.name, self.mobile = name, mobile
