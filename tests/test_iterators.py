import hypothesis
import hypothesis.strategies as st

from stargazers import first, last


@hypothesis.given(st.lists(st.integers()))
def test_first(lst):
    hypothesis.assume(len(lst) > 0)
    lst.sort()
    assert min(lst) == first(lst)


@hypothesis.given(st.lists(st.integers()))
def test_last(lst):
    hypothesis.assume(len(lst) > 0)
    lst.sort()
    assert max(lst) == last(lst)
