import os

from firebase_admin import credentials, initialize_app, auth
from app.infrastructure.auth.auth_provider import AuthProvider, AuthEmailPassword

CREDENTIALS_PATH = os.environ.get("FIREBASE_JSON_CREDENTIALS", "./assets/credentials/firebase-credentials.json")

cred = credentials.Certificate(CREDENTIALS_PATH)

initialize_app(cred)


class FirebaseAuthProvider(AuthProvider):

    def login_with_email_password(self, payload: AuthEmailPassword):
        pass

    def verify_token(self, token: str):
        pass
