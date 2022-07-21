import pytest


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print("crossBrowser")