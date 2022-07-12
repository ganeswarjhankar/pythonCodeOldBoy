import pytest


@pytest.fixture()
def setup():
    print("I will executing first")
    yield
    print("I will execute last after field")


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("i will be executing steps in fixturedemo method")
    def test_fixtureDemo2(self):
        print("i will be executing steps in fixturedemo method")

    def test_fixtureDemo3(self):
        print("i will be executing steps in fixturedemo method")


