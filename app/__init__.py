from flask import Flask
from flask_mail import Mail
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .models import db, User

login_manager = LoginManager()
login_manager.login_view = 'main.login'

mail = Mail()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    mail.init_app(app)
    socketio.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app