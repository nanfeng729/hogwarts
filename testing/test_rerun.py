from time import sleep
import pytest


def test_run1():
    sleep(0.5)
    assert 1 == 2


def test_run2():
    sleep(0.5)
    assert 2 == 2


@pytest.mark.flaky(reruns=4)
def test_run3():
    sleep(0.5)
    assert 3 == 2
