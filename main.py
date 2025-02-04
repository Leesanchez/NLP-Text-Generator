import random
from src.ngram_model import *  # Importing required functions from ngram_model module

def generate_text_from_ngram(initial_ngram, length, ngram_probs, n):
    """
    Generates text using N-gram probabilities.
    """
    current_ngram = initial_ngram
    generated_text = list(current_ngram)
    
    for _ in range(length - n):
        if current_ngram not in ngram_probs:
            break
        next_word = random.choices(list(ngram_probs[current_ngram].keys()), weights=ngram_probs[current_ngram].values())[0]
        generated_text.append(next_word)
        current_ngram = tuple(generated_text[-(n-1):])
    
    return " ".join(generated_text)

def main():
    """
    Main function to generate Shakespearean-style text using N-grams.
    """
    # Preprocess text data (Default: Shakespeare corpus)
    tokens = preprocess()
    
    if not tokens:
        print("No tokens found. Exiting.")
        return
    
    # Prompt user for N-gram size (valid options: 2, 3, or 4)
    while True:
        try:
            n = int(input("\nEnter the n-gram size (2, 3, 4): "))
            if n not in [2, 3, 4]:
                print("Invalid input. Please enter 2, 3, or 4.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number (2, 3, or 4).")
    
    print(f"\nGenerating text with {n}-grams:")
    
    # Create N-grams
    ngrams = create_ngrams(tokens, n)
    if not ngrams:
        print(f"Not enough words to form {n}-grams. Exiting.")
        return
    
    # Compute transition probabilities
    ngram_counts = from_ngram_to_next_token_counts(ngrams)
    ngram_probs = from_ngram_to_next_token_probs(ngram_counts)
    
    if not ngram_probs:
        print(f"Skipping {n}-grams. No valid probabilities found.")
        return
    
    # Generate text using N-grams
    initial_ngram = random.choice(list(ngram_probs.keys()))
    generated_text = generate_text_from_ngram(initial_ngram, 50, ngram_probs, n)
    print("Generated Text:", generated_text)

if __name__ == "__main__":
    main()
