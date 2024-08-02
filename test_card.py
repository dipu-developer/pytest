import pytest

@pytest.fixture
def setUP():
    print("####################")
    print("Browser Open")
    print("Login")
    print("Browse Product")
    yield
    print("logout")
    print("Close Browser")

    print("####################")

def test_Add(setUP):
    print("Adding card Sucessfully")

def test_Remove(setUP):
    print("Remove card Sucessfully")