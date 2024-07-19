from abc import ABC, abstractmethod

from pydantic import BaseModel, EmailStr


class AuthEmailPassword(BaseModel):
    email: EmailStr
    password: str


class UserNotFoundException(Exception):
    pass


class InvalidToken(Exception):
    pass


class AuthProvider(ABC):

    @abstractmethod
    def login_with_email_password(self, payload: AuthEmailPassword):
        pass

    @abstractmethod
    def verify_token(self, token: str):
        pass
