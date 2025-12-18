# app/__init__.py
from flask import Flask
from app.database import db
from flask_migrate import Migrate

migrate = Migrate()


def create_app(config_class='config.Config'):
    app = Flask(__name__)

    # Динамический импорт конфигурации
    if isinstance(config_class, str):
        module_name, class_name = config_class.rsplit('.', 1)
        module = __import__(module_name, fromlist=[class_name])
        config_class = getattr(module, class_name)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import bp
    app.register_blueprint(bp)

    return app