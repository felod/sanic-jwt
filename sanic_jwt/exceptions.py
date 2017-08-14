from sanic.exceptions import SanicException, Unauthorized as SanicUnauthorized, add_status_code


@add_status_code(401)
class AuthenticationFailed(SanicException):
    def __init__(self, message="Authentication failed."):
        super().__init__(message)


@add_status_code(400)
class MissingAuthorizationHeader(SanicException):
    def __init__(self, message="Authorization header not present."):
        super().__init__(message)


@add_status_code(400)
class MissingAuthorizationCookie(SanicException):
    def __init__(self, message="Authorization cookie not present."):
        super().__init__(message)


@add_status_code(400)
class InvalidAuthorizationHeader(SanicException):
    def __init__(self, message="Authorization header is invalid."):
        super().__init__(message)


@add_status_code(500)
class RefreshTokenNotImplemented(SanicException):
    def __init__(self, message="Refresh tokens have not been enabled."):
        super().__init__(message)


class Unauthorized(SanicUnauthorized):
    def __init__(self):
        super().__init__("Auth required.", "Bearer")
