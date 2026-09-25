"""Unit tests for FASTA file parsing functions in fastaclean.parser."""

import os
import tempfile
import unittest
from fastaclean import parse_fasta


class TestFastaParser(unittest.TestCase):
    """Test suite for FASTA file parsing and sequence extraction utilities."""

    def test_basic_fasta(self) -> None:
        """Test parsing a FASTA file into a header-sequence dictionary."""
        with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
            tmp.write(">seq1\nAGCT\nATGC\n")
            tmp.write(">seq2\nTCGA\nCGTA\n")
            tmp_path = tmp.name

        expected: dict[str, str] = {
            "seq1": "AGCTATGC",
            "seq2": "TCGACGTA",
        }
        result: dict[str, str] = {}
        result = parse_fasta(tmp_path)
        self.assertEqual(result, expected)

        if os.path.exists(tmp_path):
            os.remove(tmp_path)
