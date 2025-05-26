import functools
import typing

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

    return default


def last(iterable, default=_sentinel):
    """
    Return the last index of an iterable that supports indexing.
    If indexing is supported, but the iterable is empty, returns the default.
    If the default is not specified, raises the index error.
    e.g.:
    ```
    lst = [1,2,3,4]
    last(lst, None) # 4
    last([], None) # None
    last([]) # Raises
    ```
    """
    try:
        return iterable[-1]
    except IndexError:
        if default is _sentinel:
            raise

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
    - the ability to specifiy types that shouldn't be flattened. The only types that avoid being flattened are `str` and `bytes`, and this is explicitly because those types being flattened is actively harmful in almost all cases.
    - the notion of flattening to a specific level of flatness. Don't be weird; just flatten all the way down.
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
