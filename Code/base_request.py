from http import HTTPStatus

import requests
from hamcrest import assert_that, equal_to
from requests import Response

from Code.constants import RequestType


class BaseRequest:
    """An abstract class for requests"""

    def __init__(self):
        pass

    @staticmethod
    def base_request(
        request_type: RequestType,
        path: str,
        json: dict = None,
        code: HTTPStatus = HTTPStatus.OK,
    ) -> Response:
        """A base method for requests"""
        a_request = {
            RequestType.GET: requests.get,
            RequestType.POST: requests.post,
            RequestType.PUT: requests.put,
            RequestType.DELETE: requests.delete,
        }

        response = a_request[request_type](path, json=json)
        assert_that(response.status_code, equal_to(code))

        return response

    def get(self, path: str, code: HTTPStatus = HTTPStatus.OK) -> Response:
        response = self.base_request(RequestType.GET, path, code=code)

        return response

    def post(self, path: str, json: dict, code: HTTPStatus = HTTPStatus.OK) -> Response:
        response = self.base_request(RequestType.POST, path, json, code=code)

        return response

    def delete(self, path: str, code: HTTPStatus = HTTPStatus.OK) -> Response:
        response = self.base_request(RequestType.DELETE, path, code=code)

        return response