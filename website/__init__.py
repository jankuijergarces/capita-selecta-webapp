from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

DB_USER = 'fyrzfivvbn'
DB_PASS = '16S1A2Q64OGQF8A7$'
DB_HOST = 'capita-selecta-webapp-db-server.postgres.database.azure.com'
DB_NAME = 'postgres'

db = SQLAlchemy()
migrate = Migrate(db)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey123'
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgres://{DB_USER}:{DB_PASS}$@{DB_HOST}/{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
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


