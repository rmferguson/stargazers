import hypothesis
import hypothesis.strategies as st

from stargazers import first, last


# Defaults are just to make sure that an empty list doesn't fuck us.
@hypothesis.given(st.lists(st.integers()))
def test_first(lst):
    lst.sort()
    assert min(lst, default=1) == first(lst, default=1)


@hypothesis.given(st.lists(st.integers()))
def test_last(lst):
    lst.sort()
    assert max(lst, default=1) == last(lst, default=1)
