import requests
from jsonschema import validate
from schemas import JOKES_RANDOM, JOKES_SEARCH
from Resp import Resp

url_0 = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes"
headers = {
        'accept': "application/json",
        'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
        'x-rapidapi-key': "dbb526a204msh3d0ba7ac427b77cp169316jsn4c2e14478bff"
    }

querystring = {"query": "animal"}


def test_jokes_random():
    url = url_0 + "/random"
    r = requests.request("GET", url, headers=headers, params=querystring)
    response = Resp(r)
    response.assert_status_code(200).assert_headers('application/json;charset=UTF-8')
    response_body = r.json()
    validate(response_body, JOKES_RANDOM)


def test_jokes_categories():
    url = url_0 + "/categories"
    r = requests.request("GET", url, headers=headers)
    response = Resp(r)
    response.assert_status_code(200).assert_headers('application/json;charset=UTF-8')
    for resp in r.json():
        assert isinstance(resp, str)


def test_jokes_search():
    url = url_0 + "/search"
    r = requests.request("GET", url, headers=headers, params=querystring)
    response = Resp(r)
    response.assert_status_code(200).assert_headers('application/json;charset=UTF-8')
    for resp in r.json()['result']:
        validate(resp, JOKES_SEARCH)
    assert r.json()["total"] == len(r.json()['result'])
