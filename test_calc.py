import pytest
def test_login():
    print("this is working")

@pytest.mark.skip
def test_logout():
    print("this is out")

@pytest.mark.xfail
def test_demo():
    print("this is ok")
