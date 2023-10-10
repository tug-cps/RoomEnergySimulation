from app.factory import create_app

flask_app = create_app()
celery_app = flask_app.app.extensions['celery']
