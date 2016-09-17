import pytest
import responses
from django.conf import settings
from mark.api import BookmarkApi, BookmarkUserApiException


@pytest.fixture
def book_api():
    return BookmarkApi("XXXXXX")


@responses.activate
def test_create_ok(book_api):
    responses.add(
        responses.POST, "{}/bookmark/".format(settings.BOOKMARK_API),
        status=201,
        json={},
        content_type='application/json')
    assert book_api.create("http://m4u.web")


@responses.activate
def test_create_not_ok(book_api):
    responses.add(
        responses.POST, "{}/bookmark/".format(settings.BOOKMARK_API),
        status=500,
        json={"msg": "Error ..."},
        content_type='application/json')
    with pytest.raises(BookmarkUserApiException):
        book_api.create("http://m4u.web")


@responses.activate
def test_updated_ok(book_api):
    responses.add(
        responses.PUT, "{}/bookmark/{}".format(settings.BOOKMARK_API, 50),
        status=201,
        json={},
        content_type='application/json')
    assert book_api.updated(50, "http://m4u.web")


@responses.activate
def test_updated_not_ok(book_api):
    responses.add(
        responses.PUT, "{}/bookmark/{}".format(settings.BOOKMARK_API, 50),
        status=500,
        json={},
        content_type='application/json')
    with pytest.raises(BookmarkUserApiException):
        assert book_api.updated(50, "http://m4u.web")


@responses.activate
def test_delete_ok(book_api):
    responses.add(
        responses.DELETE, "{}/bookmark/{}".format(settings.BOOKMARK_API, 50),
        status=200,
        json={},
        content_type='application/json')
    assert book_api.delete(50)


@responses.activate
def test_delete_not_ok(book_api):
    responses.add(
        responses.DELETE, "{}/bookmark/{}".format(settings.BOOKMARK_API, 50),
        status=500,
        json={},
        content_type='application/json')
    with pytest.raises(BookmarkUserApiException):
        book_api.delete(50)


@responses.activate
def test_get_ok(book_api):
    responses.add(
        responses.GET, "{}/bookmark/{}".format(settings.BOOKMARK_API, 50),
        status=200,
        json={"url": "http://m4u.web", "_id": "1111"},
        content_type='application/json')
    response = book_api.get(50)
    assert response["url"] == "http://m4u.web"
    assert response["_id"] == '1111'


@responses.activate
def test_get_not_ok(book_api):
    responses.add(
        responses.GET, "{}/bookmark/{}".format(settings.BOOKMARK_API, 50),
        status=404,
        json={"message": "not found"},
        content_type='application/json')
    with pytest.raises(BookmarkUserApiException):
        book_api.get(50)
