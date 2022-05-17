from http import HTTPStatus
from random import randrange, choice

import pytest
from faker.providers.person.en import Provider as Fake

from Code.constants import InvalidPet
from Code.pet_object import Pet, Category, PetStatus


@pytest.fixture(scope="module")
def pet(api):
    """A fixture that creates a pet for tests and deletes it afterwards"""

    new_pet = Pet(
        name=choice(Fake.first_names),
        id=randrange(100),
        category=Category(id=randrange(100), name=choice(Fake.last_names)),
        status=choice(list(PetStatus)),
    )

    yield new_pet

    api.pet_id.delete(new_pet)


def test_post_pet(api, pet):
    api.pet.post(pet)


def test_get_pet_petId(api, pet):
    api.pet.post(pet)
    api.pet_id.get(pet)


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
    api.pet_id.delete(InvalidPet(invalid_id), code=status_code)
