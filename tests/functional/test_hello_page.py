import pytest
from hello_world.serve import app


@pytest.fixture(scope="module")
def test_client():
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client  # this is where the testing happens!
    ctx.pop()


@pytest.mark.xfail(reason="hello page is not yet implemented")
def test_hello_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/hello' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get("/hello")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
