from lib.users import Users
from lib.auth import Auth
from config import APP_URL, LOG, ADMIN_PASSWORD, ADMIN_USER


def test_user_permissions(login_as_admin):
    LOG.info("test_user_permissions")

    # Create new user and assign "user" role
    new_username = "rap"
    new_password = "solo"
    new_user_roles = "user"
    response = Users().create_user(APP_URL, login_as_admin, new_username,
                                   new_password)
    assert response.ok
    response_data = response.json()
    new_user_id = response_data["id"]
    assert response_data["username"] == new_username
    assert response_data["roles"] == "user"

    # Login as the newly created user
    response = Auth().login(APP_URL, new_username, new_password)
    assert response.ok
    response_data = response.json()
    access_token = response_data["access_token"]

    # Check the new user can get his own info
    response = Users().get_current_user(APP_URL, access_token)
    assert response.ok
    assert response.json()["username"] == new_username
    assert response.json()["roles"] == new_user_roles

    # Check that the newly created user CAN NOT create other users because
    # it doesn't have admin privileges
    response = Users().create_user(APP_URL, access_token, "tony", "montana")
    assert not response.ok

    # Check that the newly created user CAN NOT delete other users because
    # it doesn't have admin privileges
    response = Users().delete_user(APP_URL, access_token, new_user_id)
    assert not response.ok

    # Finally, delete the newly created user but this time use the admin account
    response = Users().delete_user(APP_URL, login_as_admin, new_user_id)
    assert response.ok
