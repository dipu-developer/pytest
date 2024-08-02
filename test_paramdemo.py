import pytest


#  Method 01
# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print("the demo fixture params", request.param)
#
# def test_login(demo_fixture):
#     print("Login Sucessfully")

# Output:
#
# test_paramdemo.py::test_login[a] ####################
# Browser Open
# Login
# Browse Product
# the demo fixture params a
# Login Sucessfully
# PASSED
# test_paramdemo.py::test_login[b] the demo fixture params b
# Login Sucessfully
# PASSEDlogout
# Close Browser
####################


#  Method 2
@pytest.mark.parametrize("a,b,final",[(1,2,3),(5,5,10),(2,2,5),(3,2,5)])
def test_login(a,b, final):
    assert a + b == final


# Output:

# test_paramdemo.py::test_login[1-2-3] ####################
# Browser Open
# Login
# Browse Product
# PASSED
# test_paramdemo.py::test_login[5-5-10] PASSED
# test_paramdemo.py::test_login[2-2-5] FAILED
# test_paramdemo.py::test_login[3-2-5] PASSEDlogout
# Close Browser
# ####################
#
#
# ====================================================== FAILURES =======================================================
# __________________________________________________ test_login[2-2-5] __________________________________________________
#
# a = 2, b = 2, final = 5
#
#     @pytest.mark.parametrize("a,b,final",[(1,2,3),(5,5,10),(2,2,5),(3,2,5)])
#     def test_login(a,b, final):
# >       assert a + b == final
# E       assert (2 + 2) == 5
#
# test_paramdemo.py:31: AssertionError
# =============================================== short test summary info ===============================================
# FAILED test_paramdemo.py::test_login[2-2-5] - assert (2 + 2) == 5
# ============================================= 1 failed, 3 passed in 0.07s =============================================
