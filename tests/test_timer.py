from time import sleep

import pytest

from stargazers.timer import Timer, TimerError

TIMER_STATIC_DURATION = 0.5


def test_timer_functionality():
    with Timer() as t:
        sleep(TIMER_STATIC_DURATION)

    assert not list(t.get_laps())
    assert t.start_time
    assert t.stop_time


def test_bad_stop():
    with pytest.raises(TimerError):
        t = Timer()
        t.stop()
    assert True
