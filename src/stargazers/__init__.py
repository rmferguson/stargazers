"""
Utility functions without better homes.

Contains iterators, object utility functions, and testing utilities.

Most of these deserve better homes.

### Relevant documentation:
- [CMDline options](https://docs.python.org/3/using/cmdline.html#environment-variables)
- [Developer Mode](https://docs.python.org/3/library/devmode.html#devmode)
- [System Flags (Dev Mode)](https://docs.python.org/3/library/sys.html#sys.flags.dev_mode)
"""

import functools
import operator
import threading
import typing

# I can't shake the feeling I'm gonna want this later
# https://docs.python.org/3/library/functools.html#functools.singledispatch

__all__ = [
    # Helpers in this file
    "current_thread_is_main",
    "dump_to_dict",
    "dilter",
    "first",
    "batched",
    "flatten",
    "windowed",
    "invariant",
]


def current_thread_is_main():
    """
    Returns if the current thread appears to be the main thread.

    That is, returns if the threading.current_thread()
    method returns the same object as the threading.main_thread() method,
    which is checked by `is` to check for identity.
    """
    # return (id(threading.current_thread()) == id(threading.main_thread()))
    return threading.current_thread() is threading.main_thread()


def dump_to_dict(obj: object, fields: typing.Sequence) -> typing.Dict[str, typing.Any]:
    """
    Helper function that takes an object and creates a dictionary of the specified fields of that object.

    Used like:
    ```python
    class Foo():
        bar = 1
        baz = True

    f_instance = Foo()
    d = dump_to_dict(f_instance, ['bar'])
    d # {'bar': 1}
    ```
    """
    f = operator.attrgetter(*fields)
    return dict(zip(fields, f(obj)))


dilter: typing.Callable = functools.partial(filter, None)
"""
Default fILTER

Works as `filter(None, iter)`.

That's it.
"""

_sentinel = object()


def first(iterable, default=_sentinel):
    """
    Return the first index of an iterable that supports indexing.
    If indexing is supported, but the iterable is empty, returns the default.
    If the default is not specified, raises the index error.
    e.g.:
    ```
    lst = [1,2,3,4]
    first(lst, None) # 1
    first([], None) # None
    first([]) # Raises
    ```
    """
    try:
        return iterable[0]
    except IndexError:
        if default is _sentinel:
            raise
    else:
        return default


# Batched was introduced in Python 3.12,
# with the strict keyword introduced in 3.13
# If the 3.12 ver is available it should be preferred
# Since it's written in C.
def batched(iterable, n, *, strict=False):
    """
    ```python
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    list(batched(data, 2))
    # [(0, 1), (2, 3), (4, 5), (6, 7), (8,)]
    ```
    """
    from itertools import islice

    if n < 1:
        raise ValueError("n must be at least one")
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError("batched(): incomplete batch")
        yield batch


def flatten(iterable):
    """
    Based on [moreitertools.collapse](https://more-itertools.readthedocs.io/en/stable/_modules/more_itertools/more.html#collapse)

    Flattens nested iterables to a single iterable

        >>> list(flatten([[1,2,3], [4,5,6]]))
        [1,2,3,4,5,6]

    Differences from moreitertools.collapse:

    This version *removes*, and *does not* support:
    - the usage of a deque. The import and usage seemed unnecessary, since the original always pops and appends to the left.
    - the ability to specifiy types that shouldn't be flattened. The only types that avoid being flattened are `str` and `bytes`.
    - the notion of flattening to a specific level of flatness. Just flatten all the way down. Don't be weird.
    """
    from itertools import repeat

    stack = []
    # Add our first node group, treat the iterable as a single node
    # Needs to be a repeat for later.
    stack.append(repeat(iterable, 1))

    while stack:
        node_group = stack.pop()
        nodes = node_group

        for node in nodes:
            if isinstance(node, (str, bytes)):
                yield node
            else:
                try:
                    # try to create child nodes
                    tree = iter(node)
                except TypeError:
                    yield node
                else:
                    # Save current location.
                    # This works because we consumed the iterable up to this point,
                    # and therefore append a partially consumed iterable.
                    stack.append(node_group)
                    # Append the new child node
                    stack.append(tree)
                    # Break to process child node
                    break


def windowed(seq, n):
    """
    Taken from [itertools recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes)

    Collect data into overlapping fixed-length chunks or blocks.

    ```python
    >>> for w in windowed('ABCDEFG', 4):
    >>>    print(w)
    ABCD
    BCDE
    CDEF
    DEFG
    ```
    """
    # Contrasting to flatten, this needs to be a deque for the maxlen property
    # that lists don't offer oob
    from collections import deque
    from itertools import islice

    iterator = iter(seq)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


class InvariantViolation(Exception):
    """
    Never actually catch this. If this is raised then there's a fundamental problem in your
    invariant declaration or your assumptions about the code.

    Fix those!
    """


@functools.singledispatch
def invariant(
    obj: object,
    test: typing.Callable[..., bool],
    msg: str | None = None,
) -> None:
    if not test(obj):
        assert callable(test)
        msg = "" if msg is None else msg[:]
        raise InvariantViolation(msg)


@invariant.register(bool)
def _(condition: bool, msg: str | None = None) -> None:
    if not condition:
        msg = "" if msg is None else msg[:]
        raise InvariantViolation(msg)


def _run_tests():
    import contextlib

    terrible_data = [
        [_ for _ in range(3)],
        [],
        [],
        "string that shouldn't be flattened",
        [_ for _ in range(3, 6)],
        [_ for _ in range(6, 9)],
        [],
        [[[_ for _ in range(9, 12)], [], [_ for _ in range(12, 15)]]],
        [[[[[["another string that shouldn't be flattened."]]]]]],
    ]

    better_data = list(flatten(terrible_data))
    for d in better_data:
        assert not isinstance(d, list)
    for i in range(15):
        assert i in better_data, i
    str_count = len(list(filter(lambda x: isinstance(x, str), better_data)))
    assert str_count == 2

    # pylint doesn't handle the single dispatch correctly.
    invariant(2 + 2 == 4)  # pylint: disable=E1120
    invariant(object, lambda x: x is not None)

    with contextlib.suppress(InvariantViolation):
        invariant(None, lambda x: x is not None)

    print("All tests passed")


if __name__ == "__main__":
    import sys

    sys.exit(_run_tests())
