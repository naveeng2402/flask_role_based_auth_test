from flask import Blueprint
from flask_login import current_user, login_required

student = Blueprint('student', __name__)

@student.before_request
# @login_required
def before_request():
    if "student" != current_user.roles[0].role_name:
        return "<h1>Unauthorized Access</h1>"
    
@student.route("/stud-home")
@login_required
def home():
    return "<h1>Student Homepage</h1>"
    