from fastapi import APIRouter, Depends, HTTPException, status

from app.infrastructure.auth.auth_provider import AuthEmailPassword, AuthProvider, InvalidCredentials
from app.infrastructure.auth.auth_manager import current_provider, verify_token

route_auth = APIRouter()


@route_auth.post("/login")
def login(payload: AuthEmailPassword,
          auth_provider: AuthProvider = Depends(current_provider)):
    try:
        return auth_provider.login_with_email_password(payload)
    except InvalidCredentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )


@route_auth.post("/check-session")
def check_session(verify=Depends(verify_token)):
    return {
        'status': 'OK'
    }