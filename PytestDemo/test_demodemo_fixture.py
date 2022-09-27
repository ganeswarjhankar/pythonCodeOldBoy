import pytest


@pytest.fixture

def setup():
    print("This is a fixture Example will be executed first")

    yield
    print("This is an example of Yield will execute last" )


def test_fixtureDemo(setup):
    print("This an example for Fixture,This will be executed at the middle")




