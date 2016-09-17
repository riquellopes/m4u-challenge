import pytest
import responses
from django.conf import settings
from mark.api import BookmarkUserApi, BookmarkUserApiException


@pytest.fixture
def user_api():
    return BookmarkUserApi()


@responses.activate
def test_login_ok(user_api):
    responses.add(
        responses.POST, "{}/user/auth".format(settings.BOOKMARK_API),
        status=200,
        json={"user": {"username": "riquellopes", "_id": 123, "is_admin": True}, "token": "xxxxxxxxx"},
        content_type='application/json')

    user_api.login("riquellopes", "1234567")
    assert user_api.id == 123
    assert user_api.username == "riquellopes"
    assert user_api.token == "xxxxxxxxx"
    assert user_api.is_admin


@responses.activate
def test_login_not_ok(user_api):
    responses.add(
        responses.POST, "{}/user/auth".format(settings.BOOKMARK_API),
        status=401,
        json={"msg": "Username or Password not set."},
        content_type='application/json')

    with pytest.raises(BookmarkUserApiException) as e:
        user_api.login(None, None)
    assert "Username or Password not set." in str(e.value)


@responses.activate
def test_create_ok(user_api):
    responses.add(
        responses.POST, "{}/user".format(settings.BOOKMARK_API),
        status=201,
        json={"msg": "User created", "user": {"username": "riquellopes", "_id": 123, "is_admin": False}},
        content_type='application/json')

    user_api.create("riquellopes", "1234567")

    assert user_api.id == 123
    assert user_api.username == "riquellopes"
    assert user_api.token is None
    assert user_api.is_admin is False


@responses.activate
def test_create_not_ok(user_api):
    responses.add(
        responses.POST, "{}/user".format(settings.BOOKMARK_API),
        status=409,
        json={"msg": "User can't be created."},
        content_type='application/json')

    with pytest.raises(BookmarkUserApiException) as e:
        user_api.create("riquellopes", "1234567")
    assert "User can't be created." in str(e.value)


@responses.activate
def test_list_user_ok(user_api):
    responses.add(
        responses.GET, "{}/user/".format(settings.BOOKMARK_API),
        status=200,
        json=[{}],
        content_type='application/json')

    result = user_api.list("XXXXXXXXX")
    assert isinstance(result, list)


@responses.activate
def test_list_user_not_ok(user_api):
    responses.add(
        responses.GET, "{}/user/".format(settings.BOOKMARK_API),
        status=401,
        json={"msg": "User is not an admin."},
        content_type='application/json')

    with pytest.raises(BookmarkUserApiException) as e:
        user_api.list("XXXXXXXXA")
    assert "User is not an admin." in str(e.value)
