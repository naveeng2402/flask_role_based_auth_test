from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

staff = Blueprint('staff', __name__)

@staff.before_request
# @login_required
def before_request():
    if "staff" != current_user.roles[0].role_name:
        return "<h1>Unauthorized Access</h1>"
    print(f"[CALLBACK] {request.path} ...")
    
@staff.route("/staff-home")
@login_required
def home():
    return "<h1>Staff Homepage</h1>"
     