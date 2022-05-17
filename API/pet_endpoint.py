import json
from http import HTTPStatus

from hamcrest import assert_that, is_in, equal_to
from pydantic import BaseModel

from Code.base_request import BaseRequest
from Code.constants import METHOD_NOT_ALLOWED_ERROR, NotFoundError
from Code.pet_object import Pet


class PetEndpoint:
    def __init__(self, path):
        self.path = path

    def post(self, data: BaseModel):
        json_data = json.loads(data.json())

        response = BaseRequest().post(self.path, json_data)
        response_json = response.json()
        expected_json = {k: v for k, v in json.loads(data.json()).items() if v}

        assert_that(response_json, equal_to(expected_json))


class PetFindByStatus:
    def __init__(self, path):
        self.path = path


class PetFindByTags:
    def __init__(self, path):
        self.path = path


class PetPetId:
    def __init__(self, path):
        self.path = path

    def get(self, pet: Pet, params: dict = None, code: HTTPStatus = HTTPStatus.OK):
        response = BaseRequest().get(f"{self.path}/{pet.id}", params=params, code=code)
        response_json = response.json()
        expected_json = {k: v for k, v in json.loads(pet.json()).items() if v}

        assert_that(response_json, equal_to(expected_json))

    def delete(self, pet_id: int, code: HTTPStatus = HTTPStatus.OK):
        response = BaseRequest().delete(f"{self.path}/{pet_id}", code=code)

        if code == HTTPStatus.OK:
            assert_that(f'"message":"{pet_id}"', is_in(response.text))
        elif code == HTTPStatus.NOT_FOUND:
            if response.text:
                error = NotFoundError()
                error.message %= pet_id
                assert_that(error.dict(), equal_to(json.loads(response.text)))
        elif code == HTTPStatus.METHOD_NOT_ALLOWED:
            assert_that(response.text, equal_to(METHOD_NOT_ALLOWED_ERROR))
        else:
            raise Exception(f"\n[ERROR] Unexpected status code! {response.status_code}")


class PetIdUploadImage:
    def __init__(self, path):
        self.path = path
