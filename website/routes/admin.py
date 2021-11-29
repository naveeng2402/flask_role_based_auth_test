from flask import Blueprint, request
from flask_login import current_user, login_required

admin = Blueprint('admin', __name__)

@admin.before_request
# @login_required
def before_request():
    print(f"[CALLBACK] {request.path} ...")
    if "admin" != current_user.roles[0].role_name:
        return "<h1>Unauthorized Access</h1>"
    
@admin.route("/admin-home")
@login_required
def home():
          return "<h1>Admin Homepage</h1>"
     