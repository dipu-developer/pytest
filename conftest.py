import pytest

# @pytest.fixture(autouse=True)
# def setUP():
#     print("####################")
#     print("Browser Open")
#     print("Login")
#     print("Browse Product")
#     yield
#     print("logout")
#     print("Close Browser")
#
#     (print("####################")

@pytest.fixture(scope="session",autouse=True)
def setUP():
    print("####################")
    print("Browser Open")
    print("Login")
    print("Browse Product")
    yield
    print("logout")
    print("Close Browser")

    print("####################")