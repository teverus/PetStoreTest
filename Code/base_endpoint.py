from Code.constants import BASE_URL


class BaseEndpoint:
    """An abstract class for endpoints"""
    def __init__(self, path):
        self.path = f"{BASE_URL}{path}"
