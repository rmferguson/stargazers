"""
### Legal
SPDX-FileCopyright © 2025 Robert Ferguson <rmferguson@pm.me>

SPDX-License-Identifier: [MIT](https://spdx.org/licenses/MIT.html)
"""

import pytest

from stargazers import InvariantViolation, invariant


def test_invariant():
    assert invariant(True)  # pylint: disable=E1120
    assert invariant(2 + 2 == 4)  # pylint: disable=E1120
    assert invariant(object, lambda x: x is not None)

    with pytest.raises(InvariantViolation):
        invariant(object(), lambda x: x is None)
    assert True
