import random
from collections import defaultdict
import nltk
import os

# Ensure necessary NLTK resources are available
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

def preprocess():
    """
    Loads and tokenizes Shakespeare's text from the manually downloaded file.
    """
    print("Loading Shakespeare texts from local file...")

    # Define file path
    corpus_root = os.path.expanduser("nltk_data/corpora/shakespeare/")
    text_file = os.path.join(corpus_root, "shakespeare.txt")

    # Check if file exists
    if not os.path.exists(text_file):
        print("Error: Shakespeare corpus file not found. Please download it first.")
        return []

    # Read and tokenize text
    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read().strip().lower()

    try:
        tokens = nltk.word_tokenize(text)
    except LookupError:
        print("NLTK tokenizer not found. Using basic split instead.")
        tokens = text.split()
    
    print(f"Extracted {len(tokens)} tokens from Shakespeare's corpus.")
    return tokens

def create_ngrams(tokens, n):
    """
    Creates N-grams from a list of tokens.
    """
    if len(tokens) < n:
        return []
    return [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]

def from_ngram_to_next_token_counts(ngrams):
    """
    Converts N-grams into a dictionary of next token counts.
    """
    ngram_counts = defaultdict(lambda: defaultdict(int))
    for gram in ngrams:
        prefix, next_word = tuple(gram[:-1]), gram[-1]
        ngram_counts[prefix][next_word] += 1
    return ngram_counts

def from_ngram_to_next_token_probs(ngram_counts):
    """
    Converts token counts into probabilities.
    """
    ngram_probs = {}
    for prefix, next_words in ngram_counts.items():
        total_count = sum(next_words.values())
        ngram_probs[prefix] = {word: count / total_count for word, count in next_words.items()}
    return ngram_probs
