#!/usr/bin/env python3


import unittest
from fastaclean.filter import (
        validate_sequence,
        min_length,
        n_percent,
        filter_sequences,
)


class TestFilter(unittest.TestCase):
    def test_validate_sequence(self) -> None:
        self.assertTrue(validate_sequence("ATCGN"))
        self.assertFalse(validate_sequence("ATXNN"))
        self.assertTrue(validate_sequence("ACcgN"))

    def test_min_length(self) -> None:
        self.assertTrue(min_length("ATCGNACTCG", 7))
        self.assertFalse(min_length("CGATAC", 7))
        self.assertFalse(min_length("", 7))

    def test_n_percent(self) -> None:
        self.assertTrue(n_percent("ATCGN", 25.0))
        self.assertFalse(n_percent("ATGNNCANNG", 20.))

    def test_filter_sequences(self) -> None:
        dataset = {
            ">seq1": "ATCGN",
            ">seq2": "ATCGX",
            ">seq3": "ATC",
            ">seq4": "ANNNN",
        }

        filtered, stats = filter_sequences(dataset,
                                           length=5,
                                           max_n_percent=30.0)

        expected_filtered = {">seq1": "ATCGN"}
        self.assertEqual(filtered, expected_filtered)

        expected_stats = {
            "initial_seq": 4,
            "conserved_seq": 1,
            "rejected_seq": 3,
        }
        self.assertEqual(stats, expected_stats)


if __name__ == "__main__":
    unittest.main()
