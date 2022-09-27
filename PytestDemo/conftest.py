import pytest

@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will be execute last")
##created  all the parameters in the  fixture and send them at runtime to the test cases which needs it during the testing runtime
@pytest.fixture()
def dataLoad():
    print("user profile data is created"  )
    return ["rahul","Shetty","rahulshetty.com"]

##To run the same test in Multiple Browsers, Here is the following Scenarios
#actural data is in chrome, there is an instace, parameter is "request"
#Need to use request parameter whenever "Fixtures with some values available"

@pytest.fixture(params=[("chrome","Rahul","Shetty"),("Firefox","Rahul","Shetty"),"IE","SS"])
def crossBrowser(request):
    return request.param





