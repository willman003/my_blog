from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'

def create_app(config_name):
    #Flask configuration
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #Initialization
    db.init_app(app)
    login_manager.init_app(app)

    #Blueprints registration
    from .authentication import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    from .blog import blog as blog_bp
    app.register_blueprint(blog_bp, url_prefix='/blog')

    return app