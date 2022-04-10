import requests
from faker import Faker
from jsonschema import validate
from schemas import GET_POSTS, GET_COMMENTS, GET_ALBUMS, GET_PHOTOS, GET_TODOS
from Resp import Resp

url = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    r = requests.get(url + "/posts")
    response = Resp(r)
    response.assert_status_code(200)
    assert len(r.json()) == 100
    for resp in r.json():
        validate(resp, GET_POSTS)


def test_get_comments():
    r = requests.get(url + "/comments")
    response = Resp(r)
    response.assert_status_code(200)
    assert len(r.json()) == 500
    for resp in r.json():
        validate(resp, GET_COMMENTS)


def test_get_albums():
    r = requests.get(url + "/albums")
    response = Resp(r)
    response.assert_status_code(200)
    assert len(r.json()) == 100
    for resp in r.json():
        validate(resp, GET_ALBUMS)


def test_get_photos():
    r = requests.get(url + "/photos")
    response = Resp(r)
    response.assert_status_code(200)
    assert len(r.json()) == 5000
    for resp in r.json():
        validate(resp, GET_PHOTOS)


def test_get_todos():
    r = requests.get(url + "/todos")
    response = Resp(r)
    response.assert_status_code(200)
    assert len(r.json()) == 200
    for resp in r.json():
        validate(resp, GET_TODOS)


def test_get_posts_1():
    r = requests.get(url + "/posts/1")
    response = Resp(r)
    response.assert_status_code(200)
    validate(r.json(), GET_POSTS)


def test_posts_1_comments():
    r = requests.get(url + "/posts/1/comments")
    response = Resp(r)
    response.assert_status_code(200)
    for resp in r.json():
        validate(resp, GET_COMMENTS)


def test_posts_comments_postId_1():
    r = requests.get(url + "/comments?postId=1")
    response = Resp(r)
    response.assert_status_code(200)
    for resp in r.json():
        validate(resp, GET_COMMENTS)


def test_post_posts():
    r = requests.post(url + "/posts", json={"userId": Faker().random_number(),
                                                                                 "title": Faker().word(),
                                                                                 "body": Faker().sentences()})
    response = Resp(r)
    response.assert_status_code(201)


def test_put_posts_1():
    r = requests.put(url + "/posts/1", json={"userId": Faker().random_number(),
                                                                                  "title": Faker().word(),
                                                                                  "body": Faker().sentences()})
    response = Resp(r)
    response.assert_status_code(200)


def test_patch_posts_1():
    r = requests.patch(url + "/posts/1", json={"userId": Faker().random_number(),
                                                                                  "title": Faker().word(),
                                                                                  "body": Faker().sentences()})
    response = Resp(r)
    response.assert_status_code(200)


def test_delete_posts_1():
    r = requests.delete(url + "/posts/1")
    response = Resp(r)
    response.assert_status_code(200)


def test_get_albums_1_photos():
    r = requests.get(url + "/albums/1/photos")
    response = Resp(r)
    response.assert_status_code(200)
    for resp in r.json():
        validate(resp, GET_PHOTOS)


def test_get_users_1_albums():
    r = requests.get(url + "/users/1/albums")
    response = Resp(r)
    response.assert_status_code(200)
    for resp in r.json():
        validate(resp, GET_ALBUMS)


def test_get_users_1_todos():
    r = requests.get(url + "/users/1/todos")
    response = Resp(r)
    response.assert_status_code(200)
    for resp in r.json():
        validate(resp, GET_TODOS)


def test_get_users_1_posts():
    r = requests.get(url + "/users/1/posts")
    response = Resp(r)
    response.assert_status_code(200)
    for resp in r.json():
        validate(resp, GET_POSTS)
