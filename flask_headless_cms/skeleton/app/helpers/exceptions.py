
class JsonException(Exception):
    """
    Handles JSON exceptions
    """
    def __init__(self, message):
        self.message = message

    def __str__(self, *args, **kwargs):
        return repr(self.message)
