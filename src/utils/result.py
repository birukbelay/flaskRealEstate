from json import JSONEncoder

from src.utils.loging import autolog, autolog_plus


class Result:
    """Represent the outcome of an operation."""
    success = bool
    def __init__(self, success, value, error):
        """Represent the outcome of an operation."""
        self.success = success
        self.error = error
        self.value = value

    @staticmethod
    def Fail(error_message):
        """Create a Result object for a failed operation."""
        autolog_plus(f"Fail=", error_message)
        return Result(False, value=None, error=error_message)

    @staticmethod
    def Ok(value=None):
        """Create a Result object for a successful operation."""
        return Result(True, value=value, error=None)

    @property
    def failure(self):
        """Flag that indicates if the operation failed."""
        return not self.success
    @property
    def succeed(self):
        """Flag that indicates if the operation failed."""
        return self.success
