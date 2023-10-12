import pytest
import webtest

from app.factory import create_app


@pytest.fixture()
def app():
    return webtest.TestApp(create_app())
