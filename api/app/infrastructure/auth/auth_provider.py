from abc import ABC, abstractmethod
from typing import Optional

from pydantic import BaseModel, EmailStr


class AuthEmailPassword(BaseModel):
    email: EmailStr
    password: str


class InvalidCredentials(Exception):
    pass


class UserNotFoundException(Exception):
    pass


class InvalidToken(Exception):
    pass


class AuthSuccessData(BaseModel):
    token_id: str
    refresh_token: str


class AuthProvider(ABC):

    @abstractmethod
    def login_with_email_password(self, payload: AuthEmailPassword) -> Optional[AuthSuccessData]:
        pass

    @abstractmethod
    def verify_token(self, token: str):
        pass
