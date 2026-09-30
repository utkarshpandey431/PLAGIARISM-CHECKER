import unittest
from main import calculate_similarity, classify_similarity, preprocess_text


class TestPlagiarismChecker(unittest.TestCase):

    def test_preprocess(self):
        self.assertEqual(preprocess_text("Hello, World!"), ["hello", "world"])

    def test_identical(self):
        self.assertEqual(calculate_similarity("hello world", "hello world"), 100.0)

    def test_partial(self):
        result = calculate_similarity("a b c", "a b d")
        self.assertAlmostEqual(result, 50.0, places=1)

    def test_different(self):
        self.assertEqual(calculate_similarity("hello", "world"), 0.0)

    def test_classify(self):
        self.assertEqual(classify_similarity(85), "High Similarity")
        self.assertEqual(classify_similarity(50), "Moderate Similarity")
        self.assertEqual(classify_similarity(10), "Low Similarity")


if _name_ == "_main_":
    unittest.main()
