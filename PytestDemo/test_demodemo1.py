import pytest


@pytest.mark.smoke
def test_firstProgram():
    msg = "Hello" #Operations
    assert msg =="Hello check ","Hi check 2nd line"

def test_secondprogram():
    a = 2
    b = 3
    assert  a+2 ==4, "Addition donot match" 