import hypothesis
import hypothesis.strategies as st

from stargazers.files import get_str_hex


@hypothesis.given(st.text())
def test_str_hex_inputs(to_hash):
    get_str_hex(to_hash)
    assert True
