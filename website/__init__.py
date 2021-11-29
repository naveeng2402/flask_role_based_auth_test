from flask import Flask
from os import path

from .extensions import db, login_manager
from .commands import create_tables
from . import routes

def create_app(config_file = "settings.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    
    db.init_app(app)
    login_manager.init_app(app)
    
    from .models import Admin, Staff, Student, User, Roles
    create_db(app)
    
    app.cli.add_command(create_tables)
    
    app.register_blueprint(routes.auth, url_prefix='/')
    app.register_blueprint(routes.admin, url_prefix='/')
    app.register_blueprint(routes.staff, url_prefix='/')
    app.register_blueprint(routes.student, url_prefix='/')
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    return app

def create_db(app: Flask):
    from .models import Roles
    
    if not path.exists("website/database.sqlite"):
        db.create_all(app=app)
        
        roles = ["admin", "staff", "student", "parent"]
        for role in roles:
            with app.app_context():
                db.session.add(Roles(role_name=role))
                db.session.commit()
        
        print("[INFO] New Database created.")
