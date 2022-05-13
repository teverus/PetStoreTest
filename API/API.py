from API.pet_endpoint import (
    PetEndpoint,
    PetFindByStatus,
    PetFindByTags,
    PetId,
    PetIdUploadImage,
)


class API:
    """A class that holds all endpoints of the application"""
    def __init__(self):
        self.pet = PetEndpoint("/pet")
        self.pet_find_by_status = PetFindByStatus("/pet/findByStatus")
        self.pet_find_by_tags = PetFindByTags("/pet/findByStatus")
        self.pet_id = PetId("/pet")
        self.pet_id_upload_image = PetIdUploadImage("/pet")
