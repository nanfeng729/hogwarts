import pytest


def test_a():
    # assert 1==1
    # assert False==True
    # assert 200==1
    pytest.assume(1 == 1)
    pytest.assume(False == True)
    pytest.assume(200 == 1)
