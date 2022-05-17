from enum import Enum
from typing import List

from pydantic import BaseModel


class Category(BaseModel):
    id: int = None
    name: str = None


class PetStatus(str, Enum):
    available = "available"
    pending = "pending"
    sold = "sold"


class Pet(BaseModel):
    id: int = None
    category: Category = None
    name: str
    photoUrls: List[str] = None
    tags: List[str] = None
    status: PetStatus = None
