import requests
from lib.utils import build_request_headers
from config import SESSION, LOG


class Users:

    def __init__(self):
        self.user_url = "/users"

    def get_all_users(self, app_url, access_token):
        LOG.info("get_all_users")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(
            f"{app_url}{self.user_url}", headers=request_headers)
        return response

    def create_user(self, app_url, access_token, username, password, role="user"):
        LOG.info("create_user")
        request_headers = build_request_headers(access_token,
                                                content_type="application/json")
        payload = {"username": username, "password_hash": password,
                   "roles": role}
        LOG.debug(f"Request payload: {payload}")
        response = SESSION.post(f"{app_url}{self.user_url}",
                                headers=request_headers, json=payload)
        return response

    def get_current_user(self, app_url, access_token):
        LOG.info("get_current_user")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(
            f"{app_url}{self.user_url}/me", headers=request_headers)
        return response

    def delete_user(self, app_url, access_token, user_id):
        LOG.info("delete_comment")
        request_headers = build_request_headers(access_token)
        response = SESSION.delete(f"{app_url}{self.user_url}/{user_id}",
                                  headers=request_headers)
        return response
