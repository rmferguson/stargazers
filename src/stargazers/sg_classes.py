import abc
import signal
from operator import attrgetter
from typing import Any

__all__ = [
    "AbstractContextManager",
    "AbstractAsyncContextManager",
    "FromJsonMixin",
    "ToJsonMixin",
    "JsonIOMixin",
    "DecimalCounterMixin",
    "HexCounterMixin",
    "KeyboardInterruptManager",
]


class FromJsonMixin(object):
    """
    A Mixin that provides a `from_mapping` and a `from_json_mapping` method.

    `from_mapping` returns an instance of the class when passed a mapping of string:Any

    `from_json_mapping` is the same, but expects that the mapping is still in a JSON str instead.
    """

    @classmethod
    def from_mapping(cls, data: dict[str, Any]):
        return cls(**data)

    @classmethod
    def from_json_mapping(cls, data: str):
        from json import loads

        return cls(**loads(data))


class ToJsonMixin(object):
    """
    A Mixin that provides the `to_json` method, which returns a dictionary of fields to values.

    For support, the class inheriting from this must implement the `_serialized_fields` static method,
    which should return a tuple of field names that will be used in the `to_json` method as keys.
    """

    @staticmethod
    def _serialized_fields():
        raise NotImplementedError

    def to_json(self):
        fields = self._serialized_fields()
        getter = attrgetter(*fields)
        return dict(zip(fields, getter(self)))


class JsonIOMixin(FromJsonMixin, ToJsonMixin):
    """
    Literally just `FromJsonMixin` and `ToJsonMixin`, together, for convenience.
    """


class _BaseCounterMixin(abc.ABC):
    @property
    @abc.abstractmethod
    def counter(self):
        raise NotImplementedError


class DecimalCounterMixin(_BaseCounterMixin):
    def __init__(self):
        self._counter = (1, 2)

    @property
    def counter(self):
        a, b = self._counter
        self._counter = b, a + b
        return a % 1000


class HexCounterMixin(_BaseCounterMixin):
    def __init__(self):
        self._counter = (1, 2)

    @property
    def counter(self):
        a, b = self._counter
        self._counter = b, a + b
        return a % 0xFFFF


try:
    from contextlib import AbstractAsyncContextManager, AbstractContextManager
except ImportError:

    class AbstractContextManager(abc.ABC):
        """
        Abstract Base Class that serves a few purposes.
        - Child classes are clearly marked as ContextManagers
        - ContextManagers in development must have the magic methods
            implemented before a class can be instantiated. (Hopefully this prevents at least one bug.)
        - It avoids the janky syntax of the built-in decorator.
        """

        @abc.abstractmethod
        def __enter__(self):
            """
            1st mandatory method for Context Managers.

            Will almost certainly look something like:
            ```python
            def __enter__(self):
                # ... Whatever other code
                # open a connection, start a timer, what-have-you.
                return self
            ```
            """
            raise NotImplementedError

        @abc.abstractmethod
        def __exit__(self, typ, val, tb):
            """
            2nd mandatory method for Context Managers.

            Way more flexible - Doesn't need to return self or anything specific.
            ```python
            def __exit__(self, typ, val, tb):
                # ... Some closing code.
                # typ - Exception type, if applicable
                # val - Exception value, if applicable
                # tb  - Traceback, if applicable
            ```
            """
            raise NotImplementedError

    class AbstractAsyncContextManager(abc.ABC):
        """
        Abstract Base Class that serves a few purposes.
        - Child classes are clearly marked as AsyncContextManagers
        - AsyncContextManagers in development must have the magic methods
            implemented before a class can be instantiated. (Hopefully this prevents at least one bug.)
        """

        @abc.abstractmethod
        async def __aenter__(self):
            """
            1st mandatory method for Async Context Managers.

            Will almost certainly look something like:
            ```python
            async def __aenter__(self):
                # ... Whatever other code
                # open a connection, start a timer, what-have-you.
                return self
            ```
            """
            raise NotImplementedError

        @abc.abstractmethod
        async def __aexit__(self, typ, val, tb):
            """
            2nd mandatory method for Async Context Managers.

            Way more flexible - Doesn't need to return self or anything specific.
            ```python
            async def __aexit__(self, typ, val, tb):
                # ... Some closing code.
                # typ - Exception type, if applicable
                # val - Exception value, if applicable
                # tb  - Traceback, if applicable
            ```
            """
            raise NotImplementedError


class KeyboardInterruptManager(AbstractContextManager):
    """
    Used in the main thread to receive a KeyboardInterrupt, but do nothing until the context ends.

    Due to how signals in python work, this can only be used in the main thread.

    Can (and should) be subclassed to give the `signal_handler` and `__exit__` method(s) any additional functionality to clean up resources.

    Note that if you're using this, you should probably be running the script through Click, or this should be in the __main__ handler.
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
            self._prev_handler(*self.signal_received)
