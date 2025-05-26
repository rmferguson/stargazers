import math

import hypothesis
import hypothesis.strategies as st

from stargazers.iter import first, flatten, last


@hypothesis.given(st.lists(st.integers()))
def test_first_w_integers(lst):
    hypothesis.assume(len(lst) > 0)
    lst.sort()
    assert min(lst) == first(lst)


@hypothesis.given(st.lists(st.integers()))
def test_last_w_integers(lst):
    hypothesis.assume(len(lst) > 0)
    lst.sort()
    assert max(lst) == last(lst)


@hypothesis.given(st.lists(st.floats().filter(lambda x: not math.isnan(x))))
def test_first_w_float(lst):
    hypothesis.assume(len(lst) > 0)
    lst.sort()
    assert min(lst) == first(lst)


@hypothesis.given(st.lists(st.floats().filter(lambda x: not math.isnan(x))))
def test_last_w_float(lst):
    hypothesis.assume(len(lst) > 0)
    lst.sort()
    assert min(lst) == first(lst)


def basic_flatten_test():
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


@hypothesis.given(st.lists(st.text()))
def test_non_flattening_of_text(lst):
    assert len(lst) == len(list(flatten(lst)))


@hypothesis.given(st.lists(st.lists(st.text())))
def test_flatten_nested_lists_of_text(lst):
    assert all(isinstance(x, str) for x in flatten((lst)))
