from dataclasses import dataclass
from typing import List

from Code.constants import PetStatus


@dataclass
class Pet:
    """Dataclass for a pet"""

    pet_name: str
    photo_urls: List = None
    pet_id: int = None
    category_id: int = None
    category_name: str = None
    tags: List = None
    status: PetStatus = None
