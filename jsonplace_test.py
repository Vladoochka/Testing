import requests
from faker import Faker
from jsonschema import validate
from schemas import Resp, GET_POSTS, GET_COMMENTS, GET_ALBUMS, GET_PHOTOS, GET_TODOS


def test_get_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    assert resp_len == 100
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_POSTS)


def test_get_comments():
    r = requests.get("https://jsonplaceholder.typicode.com/comments")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    assert resp_len == 500
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_COMMENTS)


def test_get_albums():
    r = requests.get("https://jsonplaceholder.typicode.com/albums")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    assert resp_len == 100
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_ALBUMS)


def test_get_photos():
    r = requests.get("https://jsonplaceholder.typicode.com/photos")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    assert resp_len == 5000
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_PHOTOS)


def test_get_todos():
    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    assert resp_len == 200
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_TODOS)


def test_get_users():
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    assert resp_len == 10
    for i in range(resp_len):
        assert isinstance(response_body[i]["id"], int)
        assert isinstance(response_body[i]["name"], str)
        assert isinstance(response_body[i]["email"], str)
        assert isinstance(response_body[i]["address"]["street"], str)
        assert isinstance(response_body[i]["address"]["suite"], str)
        assert isinstance(response_body[i]["address"]["city"], str)
        assert isinstance(response_body[i]["address"]["zipcode"], str)
        assert isinstance(response_body[i]["address"]["geo"]["lat"], str)
        assert isinstance(response_body[i]["address"]["geo"]["lng"], str)
        assert isinstance(response_body[i]["phone"], str)
        assert isinstance(response_body[i]["website"], str)
        assert isinstance(response_body[i]["company"]["name"], str)
        assert isinstance(response_body[i]["company"]["catchPhrase"], str)
        assert isinstance(response_body[i]["company"]["bs"], str)


def test_get_posts_1():
    r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    validate(response_body, GET_POSTS)


def test_posts_1_comments():
    r = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_COMMENTS)


def test_posts_comments_postId_1():
    r = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_COMMENTS)


def test_post_posts():
    r = requests.post("https://jsonplaceholder.typicode.com/posts", json={"userId": Faker().random_number(),
                                                                                 "title": Faker().word(),
                                                                                 "body": Faker().sentences()})
    response = Resp(r)
    response.assert_status_code(201)


def test_put_posts_1():
    r = requests.put("https://jsonplaceholder.typicode.com/posts/1", json={"userId": Faker().random_number(),
                                                                                  "title": Faker().word(),
                                                                                  "body": Faker().sentences()})
    response = Resp(r)
    response.assert_status_code(200)


def test_patch_posts_1():
    r = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json={"userId": Faker().random_number(),
                                                                                  "title": Faker().word(),
                                                                                  "body": Faker().sentences()})
    response = Resp(r)
    response.assert_status_code(200)


def test_delete_posts_1():
    r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    response = Resp(r)
    response.assert_status_code(200)


def test_get_albums_1_photos():
    r = requests.get("https://jsonplaceholder.typicode.com/albums/1/photos")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_PHOTOS)


def test_get_users_1_albums():
    r = requests.get("https://jsonplaceholder.typicode.com/users/1/albums")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_ALBUMS)


def test_get_users_1_todos():
    r = requests.get("https://jsonplaceholder.typicode.com/users/1/todos")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_TODOS)


def test_get_users_1_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/users/1/posts")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    resp_len = len(response_body)
    for i in range(resp_len):
        response_body = r.json()[i]
        validate(response_body, GET_POSTS)
