from pytest import fixture
from starlette.testclient import TestClient

from main import fast_api_app


@fixture
def test_client():
    return TestClient(fast_api_app)
