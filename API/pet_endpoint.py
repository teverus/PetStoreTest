import json
from http import HTTPStatus

from hamcrest import assert_that, is_in, equal_to

from Code.base_endpoint import BaseEndpoint
from Code.base_request import BaseRequest
from Code.helpers import get_pet_json


class PetEndpoint(BaseEndpoint):
    def __init__(self, path):
        super(PetEndpoint, self).__init__(path)

    def post(self, data: dict):
        json_data = get_pet_json(data)

        response = BaseRequest().post(self.path, json_data)
        response_json = json.loads(response.text)

        for key, value in json_data.items():
            assert_that(response_json[key], equal_to(value))


class PetFindByStatus(BaseEndpoint):
    def __init__(self, path):
        super(PetFindByStatus, self).__init__(path)


class PetFindByTags(BaseEndpoint):
    def __init__(self, path):
        super(PetFindByTags, self).__init__(path)


class PetPetId(BaseEndpoint):
    def __init__(self, path):
        super(PetPetId, self).__init__(path)

    def get(self, pet_id: int, code: HTTPStatus = HTTPStatus.OK):
        response = BaseRequest().get(f"{self.path}/{pet_id}", code=code)

        assert_that(f'"id":{pet_id}', is_in(response.text))

    def delete(self, pet_id: int, code: HTTPStatus = HTTPStatus.OK):
        response = BaseRequest().delete(f"{self.path}/{pet_id}", code=code)

        if code == HTTPStatus.OK:
            assert_that(f'"message":"{pet_id}"', is_in(response.text))


class PetIdUploadImage(BaseEndpoint):
    def __init__(self, path):
        super(PetIdUploadImage, self).__init__(path)
