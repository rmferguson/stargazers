import hypothesis
import hypothesis.strategies as st

from stargazers.sg_files import get_str_hex


@hypothesis.given(st.text())
def test_last_w_integers(txt):
    assert isinstance(get_str_hex(txt), str)
