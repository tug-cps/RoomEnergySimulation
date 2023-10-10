#!/usr/bin/env python3

import connexion

from app import encoder


def create_app():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Beyond room energy simulation API'},
                pythonic_params=True)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=8080)
