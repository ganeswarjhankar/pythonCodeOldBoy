
# Any pytest file should start with test_ format and end with _test
#method name should have sense
#-k stands for method names execution,
#-s logs in the out put
#-v stands for metadata
#You can run specific file with py.test <fielname>
#you can mark (tag)tests @pytest.mark.smoke and then run with -m
#you can skip with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used asa setup and tear down methods for teh test cases- conftest file to generalize
#fixture and make it available to all test cases

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



