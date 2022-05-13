from dataclasses import dataclass

from Code.constants import PetStatus


@dataclass
class Pet:
    """Dataclass for a pet"""
    pet_name: str
    photo_urls: list = None
    pet_id: int = None
    category_id: int = None
    category_name: str = None
    tags: list = None
    status: PetStatus = None
