"""Tests types module."""
import re

import pytest

from awpy.types import (
    int_to_string_kills,
    is_valid_side,
    lower_side,
    other_side,
    proper_kills,
    upper_side,
)


class TestTypess:
    """Class to test the awpy package types functions."""

    def test_other_side(self):
        """Tests other_side."""
        assert other_side("CT") == "T"
        assert other_side("T") == "CT"
        with pytest.raises(ValueError, match="side has to be either 'CT' or 'T'"):
            other_side("anything_else")

    def test_lower_side(self):
        """Tests lower_side."""
        assert lower_side("CT") == "ct"
        assert lower_side("T") == "t"
        with pytest.raises(ValueError, match="side has to be either 'CT' or 'T'"):
            lower_side("anything_else")

    def test_upper_side(self):
        """Tests upper_side."""
        assert upper_side("ct") == "CT"
        assert upper_side("t") == "T"
        with pytest.raises(ValueError, match="side has to be either 'ct' or 't'"):
            upper_side("anything_else")

    def test_is_valid_side(self):
        """Tests is_valid_side."""
        assert is_valid_side("CT")
        assert is_valid_side("T")
        assert not is_valid_side("anything_else")

    def test_proper_kills(self):
        """Tests proper_kills."""
        for kill in range(6):
            assert proper_kills(kill)
        assert not proper_kills(-1)
        assert not proper_kills(6)
        assert not proper_kills("A")

    def test_int_to_string_kills(self):
        """Tests int_to_string_kills."""
        for kill in range(6):
            assert int_to_string_kills(kill) == str(kill)
        with pytest.raises(ValueError, match=re.escape("kills has to be in range(6)")):
            int_to_string_kills(-1)
        with pytest.raises(ValueError, match=re.escape("kills has to be in range(6)")):
            int_to_string_kills(6)
        with pytest.raises(ValueError, match=re.escape("kills has to be in range(6)")):
            int_to_string_kills("A")
