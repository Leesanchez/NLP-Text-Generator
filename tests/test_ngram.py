import unittest
from src.ngram_model import create_ngrams, from_ngram_to_next_token_counts, from_ngram_to_next_token_probs
from src.text_generation import generate_text_from_ngram

class TestNgramModel(unittest.TestCase):
    def setUp(self):
        self.tokens = ["to", "be", "or", "not", "to", "be"]
        self.ngrams = create_ngrams(self.tokens, 2)
        self.ngram_counts = from_ngram_to_next_token_counts(self.ngrams)
        self.ngram_probs = from_ngram_to_next_token_probs(self.ngram_counts)

    def test_create_ngrams(self):
        self.assertEqual(self.ngrams, [("to", "be"), ("be", "or"), ("or", "not"), ("not", "to"), ("to", "be")])

    def test_ngram_counts(self):
        self.assertIn(("to", "be"), self.ngram_counts)
        self.assertEqual(self.ngram_counts[("to", "be")], {"or": 1, "be": 1})
    
    def test_ngram_probs(self):
        self.assertIn(("to", "be"), self.ngram_probs)
        self.assertAlmostEqual(sum(self.ngram_probs[("to", "be")].values()), 1.0)
    
    def test_generate_text(self):
        generated_text = generate_text_from_ngram(("to", "be"), 5, self.ngram_probs, 2)
        self.assertIsInstance(generated_text, str)
        self.assertGreater(len(generated_text.split()), 4)

if __name__ == "__main__":
    unittest.main()
