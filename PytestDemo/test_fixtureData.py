import pytest

@pytest.mark.usefixtures("dataLoad")

class TestExample2:

    def test_editProfile(self,dataLoad):
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])

@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
    return request.param

#request instance only use


