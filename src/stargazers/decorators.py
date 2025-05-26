import functools
import random
import time

__all__ = [
    "exponential_retry",
]


def exponential_retry(caught_exceptions=None, max_tries=3, base_delay=2):

    if caught_exceptions is None:
        caught_exceptions = (Exception,)

    def deco_retry(f):
        @functools.wraps(f)
        def f_retry(*args, **kwargs):
            tries_left = max_tries - 1
            delay = base_delay + random.uniform(0, 1)
            while tries_left > 0:
                try:
                    return f(*args, **kwargs)
                except caught_exceptions:
                    time.sleep(delay)

                    tries_left -= 1
                    expo = max_tries - tries_left
                    delay = (base_delay**expo) + random.uniform(0, 1)

            # Try last time without a catch.
            return f(*args, **kwargs)

        return f_retry

    return deco_retry
