import pytest

@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will be execute last")

@pytest.fixture()
def dataLoad():
    print("user profiler data is being created")
    return ["Rahul","Ganeswar","Jhankar.com"]

@pytest.fixture(params=["chrome","Firefox","IE"])
def crossBrowser(request):
    return request.param