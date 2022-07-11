import pytest


@pytest.fixture()
def setup():
    print("I will executing first")
    yield
    print("I will execute last after field")

def test_fixtureDemo(setup):
    print("i will be executing steps in fixturedemo method")
