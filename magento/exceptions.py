class BaseError(Exception):
    pass


class UnknownError(BaseError):
    pass


class BadRequestError(BaseError):
    pass


class UnauthorizedError(BaseError):
    pass


class ForbiddenError(BaseError):
    pass


class NotFoundError(BaseError):
    pass


class NotAllowedError(BaseError):
    pass


class NotAcceptableError(BaseError):
    pass


class SystemError(BaseError):
    pass
