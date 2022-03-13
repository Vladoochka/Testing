import requests
from jsonschema import validate
from schemas import JOKES_RANDOM, JOKES_SEARCH, Resp

headers = {
        'accept': "application/json",
        'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
        'x-rapidapi-key': "dbb526a204msh3d0ba7ac427b77cp169316jsn4c2e14478bff"
    }

querystring = {"query": "animal"}


def test_jokes_random():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
    r = requests.request("GET", url, headers=headers, params=querystring)
    response = Resp(r)
    response.assert_status_code(200).assert_headers('application/json;charset=UTF-8')
    response_body = r.json()
    validate(response_body, JOKES_RANDOM)


def test_jokes_categories():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/categories"
    r = requests.request("GET", url, headers=headers)
    response = Resp(r)
    response.assert_status_code(200).assert_headers('application/json;charset=UTF-8')
    response_body = r.json()
    resp_len = len(response_body)
    for i in range(resp_len):
        assert isinstance(response_body[i], str)


def test_jokes_search():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/search"
    r = requests.request("GET", url, headers=headers, params=querystring)
    response = Resp(r)
    response.assert_status_code(200).assert_headers('application/json;charset=UTF-8')
    response_body = r.json()['result']
    resp_len = len(response_body)
    assert r.json()["total"] == resp_len
    for i in range(resp_len):
        response_body = r.json()['result'][i]
        validate(response_body, JOKES_SEARCH)