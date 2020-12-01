import sys
import appnope


def test_nope_scope():
    with appnope.nope_scope():
        pass


def test_nope():
    assert appnope.napping_allowed()
    appnope.nope()
    assert not appnope.napping_allowed() or sys.platform != "Darwin"
    appnope.nap()
    assert appnope.napping_allowed()
