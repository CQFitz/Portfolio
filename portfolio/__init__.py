from flask import Flask
from flask_mail import Mail
from portfolio.config import Config

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)
    from portfolio.aplikasi.route import jarak
    from portfolio.aplikasi.error_handlers import errors
    app.register_blueprint(jarak)
    app.register_blueprint(errors)

    return app