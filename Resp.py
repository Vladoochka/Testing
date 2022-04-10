class Resp:
    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code
        self.response_headers = response.headers['content-type']

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code
        else:
            assert self.response_status == status_code
        return self

    def assert_headers(self, headers):
        if isinstance(headers, list):
            assert self.response_headers in headers
        else:
            assert self.response_headers == headers
        return self

    def assert_support(self):
        response_body = self.response.json()["support"]
        assert response_body['url'] == "https://reqres.in/#support-heading"
        assert response_body['text'] == "To keep ReqRes free, contributions towards server costs are appreciated!"