from src.utils.loging import autolog, autolog_forResult


class Result:
    """Represent the outcome of an operation."""

    def __init__(self, success, value, error):
        """Represent the outcome of an operation."""
        self.success = success
        self.error = error
        self.value = value

    @staticmethod
    def Fail(error_message):
        """Create a Result object for a failed operation."""
        autolog_forResult("Fail", error_message)
        return Result(False, value=None, error=error_message)

    @staticmethod
    def Ok(value=None):
        """Create a Result object for a successful operation."""
        return Result(True, value=value, error=None)

    @staticmethod
    def Combine(results):
        """Return a Result object based on the outcome of a list of Results."""
        if all(result.success for result in results):
            return Result.Ok()
        errors = [result.error for result in results if result.failure]
        return Result.Fail("\n".join(errors))


    @property
    def failure(self):
        """Flag that indicates if the operation failed."""
        return not self.success

    def on_success(self, func, *args, **kwargs):
        """Pass result of successful operation (if any) to subsequent function."""
        if self.failure:
            return self
        if self.value:
            return func(self.value, *args, **kwargs)
        return func(*args, **kwargs)
    def on_failure(self, func, *args, **kwargs):
        """Pass error message from failed operation to subsequent function."""
        if self.success:
            return self.value if self.value else None
        if self.error:
            return func(self.error, *args, **kwargs)
        return func(*args, **kwargs)

    def on_both(self, func, *args, **kwargs):
        """Pass result (either succeeded/failed) to subsequent function."""
        if self.value:
            return func(self.value, *args, **kwargs)
        return func(*args, **kwargs)