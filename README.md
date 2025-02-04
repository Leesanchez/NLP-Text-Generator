# 📜 Shakespearean N-Gram Text Generator

## **Overview**
This project is a **Shakespearean-style text generator** using **N-grams** (bigrams, trigrams, or four-grams). The model is trained on Shakespeare's complete works from **Project Gutenberg**.

## **How It Works**
- Loads and tokenizes **Shakespeare’s works** from a manually downloaded text file.
- Uses an **N-gram model** to generate Shakespeare-like sentences.
- Allows the user to **select the N-gram size** (2, 3, or 4).
- Outputs a random **Shakespearean-style text sample**.

## **Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/NLP-Text-Generator.git
cd NLP-Text-Generator
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Download the Shakespeare Corpus**
Manually download Shakespeare’s full works:
```bash
mkdir -p nltk_data/corpora/shakespeare
curl -o nltk_data/corpora/shakespeare/shakespeare.txt https://www.gutenberg.org/cache/epub/100/pg100.txt
```

## **Usage**
Run the program:
```bash
python main.py
```
Follow the prompts to **select an N-gram size** (2, 3, or 4), and the script will generate a text sample.

## **Example Output**
```
Enter the n-gram size (2, 3, 4): 3
Generating text with 3-grams:
Generated Text: womanhood. think, we are convented upon a wretch whose natural gifts were poor and speech unable; beyond all talents. whilst i go to ’t well, protect yourself. king henry...
```

## **Project Structure**
```
NLP-Text-Generator/
│-- src/
│   │-- ngram_model.py  # Handles text processing & N-gram logic
│-- data/
│   │-- shakespeare.txt  # Downloaded Shakespeare text
│-- main.py  # Runs the text generator
│-- tests/
│   │-- test_ngram.py  # Unit tests
│-- requirements.txt  # Dependencies
│-- README.md  # Documentation
```

## **Running Tests**
```bash
python -m unittest discover tests/
```

## **Next Steps & Future Work**
- Convert the project into a **web app** using Flask.
- Train a **deep learning model (LSTM or GPT-2)** instead of N-grams.
- Improve punctuation handling and sentence coherence.
- Deploy as a **Shakespearean chatbot**!

## **License**
MIT License.

---
🚀 **Created by Anthony-Lee Sánchez**