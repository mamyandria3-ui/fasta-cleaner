"""Unit tests for sequence cleaning and metric calculation functions."""

import unittest
from fastaclean import (
    clean_sequence,
    gc_content,
    len_sequence,
    n_content,
)


class TestMetrics(unittest.TestCase):
    """Test suite for sequence processing and metric calculation functions."""

    def test_clean_sequence(self) -> None:
        """Test sequence cleaning."""
        """whitespace removal, and uppercase conversion."""
        self.assertEqual(clean_sequence("a t c g\n"), "ATCG")
        self.assertEqual(clean_sequence(""), "")

    def test_len_sequence(self) -> None:
        """Test sequence length calculation following whitespace cleanup."""
        self.assertEqual(len_sequence("ATCG\n"), 4)
        self.assertEqual(len_sequence(""), 0)

    def test_gc_content(self) -> None:
        """Test GC content percentage calculation."""
        self.assertEqual(gc_content("ATCG"), 50.0)
        self.assertEqual(gc_content("AAAA"), 0.0)
        self.assertEqual(gc_content(""), 0.0)

    def test_n_content(self) -> None:
        """Test ambiguous base ('N') percentage calculation."""
        self.assertEqual(n_content("ATNG"), 25.0)
        self.assertEqual(n_content("ATCG"), 0.0)
        self.assertEqual(n_content(""), 0.0)
