import pytest
from registration.registration import add_user, initialize_users


def test_add_new_user():
    users = initialize_users()
    result = add_user(users, "new_user", "new_password")
    assert result == "New user new_user has been added successfully."
    assert "new_user" in users
    assert users["new_user"] == "new_password"


def test_add_existing_user():
    users = initialize_users()
    result = add_user(users, "user1", "password1")
    assert result == "A user with this login already exists."
    assert users["user1"] == "password1"