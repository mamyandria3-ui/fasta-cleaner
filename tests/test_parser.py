#!/usr/bin/env python3

import unittest
import tempfile
import os
from fastaclean.parser import parse_fasta


class TestFastaParser(unittest.TestCase):
    def test_basic_fasta(self) -> None:
        with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
            tmp.write(">seq1\nAGCT\nATGC\n")
            tmp.write(">seq2\nTCGA\nCGTA\n")
            tmp_path = tmp.name
        expected: dict[str, str] = {"seq1": "AGCTATGC",
                                    "seq2": "TCGACGTA"}
        result: dict[str, str] = {}
        result = parse_fasta(tmp_path)
        self.assertEqual(result, expected)
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()
