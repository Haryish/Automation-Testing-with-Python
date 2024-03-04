import pytest


@pytest.fixture
def initiateBuild():
    print("This test initates build")
    yield
    print("This test closes the build")
