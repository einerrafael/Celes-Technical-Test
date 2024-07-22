from unittest.mock import MagicMock, Mock

import pytest
import requests_mock

from app.infrastructure.auth.auth_provider import AuthEmailPassword, AuthSuccessData, InvalidCredentials
from app.infrastructure.auth.firebase_auth_provider import FirebaseAuthProvider
from app.infrastructure.commons.http_client import HttpClient
from app.infrastructure.config.settings import environment_settings

# Mock settings
environment_settings.FIREBASE_WEB_API_KEY = 'fake_api_key'


@pytest.fixture
def http_client():
    return HttpClient()


def test_login_with_email_password_success(http_client):

    payload = AuthEmailPassword(email='test@example.com', password='password123')

    auth_provider = FirebaseAuthProvider(http_client)

    mock_response_data = {
        "idToken": "fake_id_token",
        "refreshToken": "fake_refresh_token"
    }

    http_client.post = MagicMock(return_value=Mock(ok=True, status=200, json=lambda: mock_response_data))

    result = auth_provider.login_with_email_password(payload)

    assert isinstance(result, AuthSuccessData)
    assert result.token_id == "fake_id_token"
    assert result.refresh_token == "fake_refresh_token"


def test_login_with_email_password_invalid_credentials(http_client):
    payload = AuthEmailPassword(email='test@example.com', password='wrongpassword')

    auth_provider = FirebaseAuthProvider(http_client)

    http_client.post = MagicMock(return_value=Mock(ok=False))

    with pytest.raises(InvalidCredentials):
        auth_provider.login_with_email_password(payload)