from flask import Blueprint, request, render_template, redirect, url_for
from flask_login.utils import login_required
from sqlalchemy.orm.query import Query
from flask_login import login_user, logout_user, current_user

from ..models import Admin, Roles, Staff, Student, User, UserRoles
from ..extensions import db


auth = Blueprint("auth", __name__)


@auth.route("/register")
def register_user():
    return render_template("register.html")


@auth.route("/register-form", methods=["POST"])
def register_form():
    uname = request.form.get("username")
    pwd = request.form.get("password")
    role = request.form.get("role")
    mobile = request.form.get("mobile")

    print(role)

    if role == "student":
        data = Student(name=uname, mobile=mobile)
        db.session.add(data)
        db.session.commit()
        data_id = Query([Student], session=db.session).all()[-1].id
        role_db: Roles = (
            Query([Roles], session=db.session).filter_by(role_name="student").first()
        )
        user = User(username=uname, pwd=pwd, data_id=data_id)
        user.roles = [role_db,]
        db.session.add(user)
        db.session.commit()
        # user_id = Query([User], session=db.session).all()[-1].id
        # rel = UserRoles(
        #     user_id=user_id,
        #     role_id=role_db.id,
        # )
    elif role == "staff":
        data = Staff(name=uname, mobile=mobile)
        db.session.add(data)
        db.session.commit()
        data_id = Query([Staff], session=db.session).all()[-1].id
        role_db: Roles = (
            Query([Roles], session=db.session).filter_by(role_name="staff").first()
        )
        user = User(username=uname, pwd=pwd, data_id=data_id)
        user.roles=[role_db,]
        db.session.add(user)
        db.session.commit()
        # user_id = Query([User], session=db.session).all()[-1].id
        # rel = UserRoles(
        #     user_id=user_id,
        #     role_id=Query([Roles], session=db.session)
        #     .filter_by(role_name="staff")
        #     .first()
        #     .id,
        # )
    else:
        data = Admin(name=uname, mobile=mobile)
        db.session.add(data)
        db.session.commit()
        data_id = Query([Admin], session=db.session).all()[-1].id
        role_db: Roles = (
            Query([Roles], session=db.session).filter_by(role_name="admin").first()
        )
        user = User(username=uname, pwd=pwd, data_id=data_id)
        user.roles = [role_db,]
        db.session.add(user)
        db.session.commit()
        # user_id = Query([User], session=db.session).all()[-1].id
        # rel = UserRoles(
        #     user_id=user_id,
        #     role_id=Query([Roles], session=db.session)
        #     .filter_by(role_name="admin")
        #     .first()
        #     .id,
        # )

    # db.session.add(rel)
    db.session.commit()

    print("[INFO] User added.")

    return redirect(url_for("auth.register_user"))


@auth.route("/sign-in")
def sign_in():
    return render_template("sign-in.html")


@auth.route("/sign-in-form", methods=["POST"])
def sign_in_form():
    uname = request.form.get("username")
    pwd = request.form.get("password")

    user: User = (
        Query([User], session=db.session).filter_by(username=uname, pwd=pwd).first()
    )
    if not user:
        return f"<h1>Invalid Credentials</h1>\n<p>{uname}</p><p>{pwd}</p>"
    login_user(user, remember=False)

    return f"<h1> username: {user.username} ; pwd: {user.pwd}, roles: {user.roles}</h1>"


@auth.route("/sign-out")
@login_required
def sign_out():
    logout_user()
    return redirect(url_for("auth.sign_in"))
