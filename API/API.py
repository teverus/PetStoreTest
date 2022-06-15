from API.pet_endpoint import (
    PetEndpoint,
    PetFindByStatus,
    PetFindByTags,
    PetPetId,
    PetIdUploadImage,
)
from Code.constants import BASE_URL


class API:
    """A class that holds all endpoints of the application"""

    def __init__(self):
        self.pet = PetEndpoint(f"{BASE_URL}/pet")
        self.pet_find_by_status = PetFindByStatus(f"{BASE_URL}/pet/findByStatus")
        self.pet_find_by_tags = PetFindByTags(f"{BASE_URL}/pet/findByTags")
        self.pet_id = PetPetId(f"{BASE_URL}/pet")
        self.pet_id_upload_image = PetIdUploadImage(f"{BASE_URL}/pet")
