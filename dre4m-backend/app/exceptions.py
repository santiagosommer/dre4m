class MissingEnvironmentVariableError(Exception):
    """Exception raised when a required environment variable is missing."""

    def __init__(self, variable_name: str):
        self.variable_name = variable_name
        super().__init__(
            f"Missing required environment variable: {variable_name}")


class InitDatabaseError(Exception):
    """Exception raised when an error occurs during database initialization."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(f"Error initializing database: {message}")


# Users exceptions
class UserAlreadyExistsError(Exception):
    """Exception raised when a user already exists in the database"""

    def __init__(self, message: str):
        self.message = message
        super().__init__(f"Error creating user: {message}")


# Auth exceptions
class NotAuthorizedUserError(Exception):
    """Exceptions raised when a user is not authorized"""

    def __init__(self, message: str):
        self.message = message
        super().__init__(f"User is not authorized: {message}")
