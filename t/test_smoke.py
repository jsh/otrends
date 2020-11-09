#!/usr/bin/env python3
"""
A stub.
"""

import pytest


def test_success() -> None:
    """Succeed."""
    assert True


def test_fail() -> None:
    """Catch an exception."""
    with pytest.raises(AssertionError):
        assert False
