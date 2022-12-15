from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    migrate = Migrate(db, app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fyrzfivvbn:16S1A2Q64OGQF8A7$@capita-selecta-webapp-db-server.postgres.database.azure.com/postgres'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

