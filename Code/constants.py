from pydantic import BaseModel

BASE_URL = "https://petstore.swagger.io/v2"
METHOD_NOT_ALLOWED_ERROR = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><apiResponse><type>unknown</type></apiResponse>'
NOT_FOUND_ERROR = '{"code":404,"type":"unknown","message":"java.lang.NumberFormatException: For input string: "%s""}'


class PetStatus:
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"

    ALL = [AVAILABLE, PENDING, SOLD]


class RequestType:
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
    OPTIONS = "options"
    HEAD = "head"
    PATCH = "patch"


class NotFoundError(BaseModel):
    code: int = 404
    type: str = "unknown"
    message: str = 'java.lang.NumberFormatException: For input string: "%s"'


class DeleteSuccess(BaseModel):
    code: int = 200
    type: str = "unknown"
    message: str = "%s"


class InvalidPet:
    def __init__(self, id):
        self.id = id
