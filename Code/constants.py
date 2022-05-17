BASE_URL = "https://petstore.swagger.io/v2"


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
