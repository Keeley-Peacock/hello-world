import pytest
from hello_world.serve import app


@pytest.fixture(scope="module")
def test_client():
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client  # this is where the testing happens!
    ctx.pop()


def test_index_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Keeley thinks that you smell" in response.data
    assert b"You should bath" in response.data
