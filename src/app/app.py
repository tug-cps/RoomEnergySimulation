import connexion
from celery import Celery
from celery import Task
from flask import Flask

from app import encoder


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app


def create_app():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_provider_class = encoder.JSONEncoder
    app.app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://localhost",
            result_backend="redis://localhost",
            task_ignore_result=True,
        )
    )
    app.app.config.from_prefixed_env()
    celery_init_app(app.app)
    app.add_api('openapi.yaml',
                arguments={'title': 'Beyond room energy simulation API'},
                pythonic_params=True)
    return app
