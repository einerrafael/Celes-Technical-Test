import json
import os

import requests
from firebase_admin import credentials, initialize_app, auth
from app.infrastructure.auth.auth_provider import AuthProvider, AuthEmailPassword, AuthSuccessData, InvalidCredentials
from app.infrastructure.config.settings import environment_settings

CREDENTIALS_PATH = os.environ.get("FIREBASE_JSON_CREDENTIALS", "./assets/credentials/firebase-credentials.json")

cred = credentials.Certificate(CREDENTIALS_PATH)

initialize_app(cred)


class FirebaseAuthProvider(AuthProvider):
    gcloud_identity_url = "https://identitytoolkit.googleapis.com/v1"
    firebase_api_key = environment_settings.FIREBASE_WEB_API_KEY or ''

    def login_with_email_password(self, payload: AuthEmailPassword):
        full_url = f"{self.gcloud_identity_url}/accounts:signInWithPassword?key={self.firebase_api_key}"

        payload = json.dumps({
            "email": payload.email,
            "password": payload.password,
            "returnSecureToken": True
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", full_url, headers=headers, data=payload)

        if response.ok:
            json_data = response.json()

            return AuthSuccessData(
                token_id=json_data['idToken'],
                refresh_token=json_data['refreshToken']
            )
        else:
            raise InvalidCredentials()

    def verify_token(self, token: str):
        decoded_token = auth.verify_id_token(token)
        return decoded_token
