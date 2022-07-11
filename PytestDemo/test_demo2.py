import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello" #Operations
    assert msg =="Hello check ","Hi check 2nd line"



def test_secondcreditcard():
    a = 2
    b = 3
    assert  a+2 ==4, "Addition donot match"

@pytest.fixture()
def setup():
    print("I will executing first")
def test_fixtureDemo(setup):
    print("i will be executing steps in fixturedemo method")



