from fastapi import HTTPException, status


class ShopException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(ShopException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class IncorrectEmailOrPasswordException(ShopException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта или пароль"


class TokenExpiredException(ShopException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Срок действия токена истек"


class TokenAbsentException(ShopException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenFormatException(ShopException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class UserIsNotPresentException(ShopException):
    status_code = status.HTTP_401_UNAUTHORIZED


class UserIsNotManager(ShopException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Пользователь не обладает правами менеджера"


class ProviderAlreadyExistsException(ShopException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Провайдер уже существует"


class ProductAlreadyExistsException(ShopException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Продукт уже существует"


