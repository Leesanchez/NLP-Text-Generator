N-Gram Shakespearean Text Generator

Overview

This project generates text in Shakespearean style using an N-Gram model. It allows users to choose between bigrams, trigrams, and four-grams for text generation.

Features

Preprocesses text into tokens

Generates N-grams (2, 3, or 4)

Computes probability distributions for text generation

Outputs a random sequence of text based on the N-gram model

Dependencies

Ensure you have the following installed:

pip install nltk

Running the Script

Execute the script using:

python main.py

The script will prompt for an N-gram size (2, 3, or 4) and generate a text sample.

Project Structure

|-- src/
|   |-- ngram_model.py  # N-gram generation functions
|   |-- text_generation.py  # Text synthesis functions
|-- data/
|   |-- shakespeare.txt  # Input text corpus
|-- main.py  # Entry point for text generation
|-- README.md  # Documentation
|-- tests/
|   |-- test_ngram.py  # Unit tests

License

MIT License

