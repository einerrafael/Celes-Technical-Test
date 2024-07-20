from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.infrastructure.auth.auth_provider import AuthProvider
from app.infrastructure.auth.firebase_auth_provider import FirebaseAuthProvider

security = HTTPBearer()


class AuthProviderFactory:

    @staticmethod
    def get_current_auth_provider() -> AuthProvider:
        return FirebaseAuthProvider()


def current_provider():
    return AuthProviderFactory.get_current_auth_provider()


def verify_token(auth_c: HTTPAuthorizationCredentials = Depends(security),
                 provider: AuthProvider = Depends(current_provider)):
    try:
        provider.verify_token(auth_c.credentials)
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No Authenticated"
        )
