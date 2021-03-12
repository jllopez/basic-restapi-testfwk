import pytest
import requests
from config import SESSION, APP_URL, ADMIN_USER, ADMIN_PASSWORD, LOG
from lib.auth import Auth


@pytest.fixture(scope="session")
def login_as_admin():
    LOG.info("login_as_admin")
    response = Auth().login(APP_URL, ADMIN_USER, ADMIN_PASSWORD)
    assert response.ok

    access_token = response.json()["access_token"]
    yield access_token
