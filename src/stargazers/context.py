import signal
from contextlib import AbstractContextManager

__all__ = [
    "KeyboardInterruptManager",
]


class KeyboardInterruptManager(AbstractContextManager):
    """
    Used in the main thread to receive a KeyboardInterrupt, but do nothing until the context ends.

    Note that if you're using this, you should probably be running the script through Click instead, or this should be in the __main__ handler.

    Due to how signals in python work, this can only be used in the main thread.

    Can (and should) be subclassed to give the `__exit__` method(s) any additional functionality to clean up resources.
    """

    def __init__(self):
        self.signal_received = None
        self._prev_handler = None
        super().__init__()

    def signal_handler(self, received_sig, frame):
        self.signal_received = (received_sig, frame)

    def __enter__(self):
        self.signal_received = None
        self._prev_handler = signal.getsignal(signal.SIGINT)
        signal.signal(signal.SIGINT, self._prev_handler)
        return self

    def __exit__(self, typ, val, tb):
        signal.signal(signal.SIGINT, self._prev_handler)
        if self.signal_received:
            self._prev_handler(*self.signal_received)  # type: ignore
