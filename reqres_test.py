import requests
from jsonschema import validate
from schemas import SINGLE_USER, SINGLE_RESOURCE, DELAYED_RESPONSE, Resp


def test_list_users():
    r = requests.get("https://reqres.in/api/users?page=2")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    validate(response_body, DELAYED_RESPONSE)
    response_body = r.json()['data']
    resp_len = len(response_body)
    for i in range(resp_len):
        response_body = r.json()['data'][i]
        validate(response_body, SINGLE_USER)
    response.assert_support()


def test_single_user():
    r = requests.get("https://reqres.in/api/users/2")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()['data']
    validate(response_body, SINGLE_USER)
    response.assert_support()


def test_single_user_not_found():
    r = requests.get("https://reqres.in/api/users/23")
    response = Resp(r)
    response.assert_status_code(404)
    response_body = r.json()
    assert isinstance(response_body, dict)


def test_list_resource():
    r = requests.get("https://reqres.in/api/unknown")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    validate(response_body, DELAYED_RESPONSE)
    response_body = r.json()['data']
    resp_len = len(response_body)
    for i in range(resp_len):
        response_body = r.json()['data'][i]
        validate(response_body, SINGLE_RESOURCE)
    response.assert_support()


def test_single_resource():
    r = requests.get("https://reqres.in/api/unknown/2")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()["data"]
    validate(response_body, SINGLE_RESOURCE)
    response.assert_support()


def test_single_resource_not_found():
    r = requests.get("https://reqres.in/api/unknown/23")
    response = Resp(r)
    response.assert_status_code(404)
    response_body = r.json()
    assert isinstance(response_body, dict)


def test_create():
    r = requests.post("https://reqres.in/api/users", json={"name": "morpheus", "job": "leader"})
    response = Resp(r)
    response.assert_status_code(201)


def test_put_update():
    r = requests.put("https://reqres.in/api/users/2", json={"name": "morpheus", "job": "zion resident"})
    response = Resp(r)
    response.assert_status_code(200)


def test_patch_update():
    r = requests.put("https://reqres.in/api/users/2", json={"name": "morpheus", "job": "zion resident"})
    response = Resp(r)
    response.assert_status_code(200)


def test_delete():
    r = requests.delete("https://reqres.in/api/users/2")
    assert r.status_code == 204


def test_register_successful():
    r = requests.post("https://reqres.in/api/register",
                             json={"email": "eve.holt@reqres.in", "password": "pistol"})
    response = Resp(r)
    response.assert_status_code(200)


def test_register_unsuccessful():
    r = requests.post("https://reqres.in/api/register", json={"email": "sydney@fife"})
    response = Resp(r)
    response.assert_status_code(400)


def test_login_successful():
    r = requests.post("https://reqres.in/api/login",
                             json={"email": "eve.holt@reqres.in", "password": "cityslicka"})
    response = Resp(r)
    response.assert_status_code(200)


def test_login_unsuccessful():
    r = requests.post("https://reqres.in/api/login", json={"email": "peter@klaven"})
    response = Resp(r)
    response.assert_status_code(400)


def test_delayed_response():
    r = requests.get("https://reqres.in/api/users?delay=3")
    response = Resp(r)
    response.assert_status_code(200)
    response_body = r.json()
    validate(response_body, DELAYED_RESPONSE)
    response_body = r.json()['data']
    resp_len = len(response_body)
    for i in range(resp_len):
        response_body = r.json()['data'][i]
        validate(response_body, SINGLE_USER)
    response.assert_support()
