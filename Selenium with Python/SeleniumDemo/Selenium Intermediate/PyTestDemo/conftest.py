import pytest


@pytest.fixture
def initiateBuild():
    print("This test initates current build")
    yield
    print("This test closes the current build")


@pytest.fixture(scope="class")
def initiateNewBuild():
    print("This test initates new build")
    yield
    print("This test closes the new build")


@pytest.fixture
def dataLoad():
    print("Fetching Data from Config File")
    return ["Haryish", "Elangumaran", "24"]


@pytest.fixture(params=["chrome", "firefox", ["Edge", "V0.1"]])
def parameter(request):
    print("Printing the parameters")
    return request.param
