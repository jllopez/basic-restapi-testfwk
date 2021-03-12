import requests
from lib.utils import build_request_headers
from config import SESSION, LOG


class Auth:

    def __init__(self):
        self.auth_url = "/auth"

    def login(self, app_url, username, password):
        LOG.info("login")
        request_headers = {"Content-Type": "application/x-www-form-urlencoded",
                           "accept": "application/json"}
        payload = {"username": username, "password": password}
        LOG.debug(f"Request payload: {payload}")
        response = SESSION.post(
            f"{app_url}{self.auth_url}/login", headers=request_headers, data=payload)
        return response
