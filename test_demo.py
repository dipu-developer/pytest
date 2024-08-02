import pytest


def test_login():
    print("this is working")
def test_logout():
    print("this is out")

@pytest.mark.sanity
def test_demo():
    print("this is ok")
