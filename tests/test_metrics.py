import unittest
from fastaclean.metrics import clean_sequence, len_sequence, gc_content, n_content


class TestMetrics(unittest.TestCase):
    def test_clean_sequence(self) -> None:
        self.assertEqual(clean_sequence("a t c g\n"), "ATCG")
        self.assertEqual(clean_sequence(""), "")

    def test_len_sequence(self) -> None:
        self.assertEqual(len_sequence("ATCG\n"), 4)
        self.assertEqual(len_sequence(""), 0)

    def test_gc_content(self) -> None:
        self.assertEqual(gc_content("ATCG"), 50.0)
        self.assertEqual(gc_content("AAAA"), 0.0)
        self.assertEqual(gc_content(""), 0.0)

    def test_n_content(self) -> None:
        self.assertEqual(n_content("ATNG"), 25.0)
        self.assertEqual(n_content("ATCG"), 0.0)
        self.assertEqual(n_content(""), 0.0)


if __name__ == "__main__":
    unittest.main()
