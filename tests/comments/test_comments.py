import pytest
import requests
from lib.utils import build_request_headers
from lib.comments import Comments
from config import APP_URL, LOG


def test_get_all_comments(login_as_admin):
    LOG.info("test_get_all_comments")
    response = Comments().get_all_comments(APP_URL, login_as_admin)
    LOG.debug(response.json())
    assert response.ok


def test_cud_comment(login_as_admin):
    LOG.info("test_cud_comment")
    response = Comments().create_comment(APP_URL, login_as_admin, "first post")
    assert response.ok
    response_data = response.json()
    comment_id = response_data["id"]
    LOG.debug(response_data)
    assert response_data["comment_text"] == "first post"

    response = Comments().update_comment(APP_URL, login_as_admin, comment_id,
                                         message="updated to second post",
                                         likes=3
                                         )
    assert response.ok
    response_data = response.json()
    LOG.debug(response_data)
    assert response_data["comment_text"] == "updated to second post"
    assert response_data["likes"] == 3

    response = Comments().delete_comment(APP_URL, login_as_admin, comment_id)
    assert response.ok
    response_data = response.json()
    LOG.debug(response_data)
    assert response_data["detail"] == f"Deleted comment {comment_id}"
