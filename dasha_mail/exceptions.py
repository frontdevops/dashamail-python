class DashaMailException(Exception):
    def __init__(self, message: str, response: dict | None = None, code: int = 0) -> None:
        super().__init__(message)
        self.response = response
        self.code = code
