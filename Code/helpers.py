import random
import string

from Code.constants import PetStatus
from Code.pet_object import Pet


def get_pet_json(data: Pet) -> dict:
    """A helper method to turn a Pet object into a JSON"""
    json = {
        "name": data.pet_name,
    }

    if data.pet_id:
        json["id"] = data.pet_id

    if data.category_id and data.category_name:
        json["category"] = {"id": data.category_id, "name": data.category_name}

    if data.photo_urls:
        json["photoUrls"] = data.photo_urls

    if data.tags:
        json["tags"] = data.tags

    if data.status:
        json["status"] = data.status

    return json


def get_random_string(
    length: int = 10, lower: bool = True, upper: bool = False, digits: bool = False
) -> str:
    """A helper method to get a random string of a specific length with specific characters"""
    options = []
    if lower:
        options += string.ascii_lowercase
    if upper:
        options += string.ascii_uppercase
    if digits:
        options += string.digits

    if options:
        return "".join(random.choice(options) for _ in range(length))
    else:
        raise Exception(
            "\n[ERROR] You must choose at least one from lower, upper or digits!"
        )


def get_random_pet_status() -> PetStatus:
    """A helper method to get a random pet status"""
    return random.choice(PetStatus.ALL)
