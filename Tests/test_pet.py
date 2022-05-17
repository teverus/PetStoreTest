from http import HTTPStatus
from random import randrange

import pytest

from Code.helpers import get_random_string, get_random_pet_status
from Code.pet_object import Pet


@pytest.fixture(scope="module")
def pet(api):
    """A fixture that creates a pet for tests and deletes it afterwards"""
    random_id = randrange(5)
    random_name = get_random_string()
    random_category_id = randrange(5)
    random_category = get_random_string()
    random_status = get_random_pet_status()

    new_pet = Pet(
        pet_id=random_id,
        pet_name=random_name,
        category_id=random_category_id,
        category_name=random_category,
        status=random_status,
    )

    yield new_pet

    api.pet_id.delete(new_pet.pet_id)


def test_post_pet(api, pet):
    api.pet.post(pet)


def test_get_pet_petId(api, pet):
    api.pet.post(pet)
    api.pet_id.get(pet.pet_id)


@pytest.mark.parametrize(
    "invalid_id, status_code",
    [
        (-1, HTTPStatus.NOT_FOUND),
        (12345678901234567890, HTTPStatus.NOT_FOUND),
        ("a", HTTPStatus.NOT_FOUND),
        ("", HTTPStatus.METHOD_NOT_ALLOWED),
    ],
)
def test_delete_pet_petID_negative(api, invalid_id, status_code):
    api.pet_id.delete(invalid_id, code=status_code)
