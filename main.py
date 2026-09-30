"""
Plagiarism Checker - Python Essentials Project
Author: Utkarsh Kumar Pandey (26BAI10231)
Compares two text inputs and calculates Jaccard similarity.
"""
import json
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_config(path="config.json"):
    """Load thresholds from config.json."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("config.json not found. Using defaults.")
        return {"high_threshold": 70, "moderate_threshold": 40}


CONFIG = load_config()


def preprocess_text(text):
    """Clean text: lowercase, keep alphabets and spaces, return word list."""
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    cleaned = ""
    for char in text:
        if char.isalpha() or char.isspace():
            cleaned += char.lower()
    return cleaned.split()


def count_words_recursive(words, index=0, word_count=None):
    """Recursively count word frequency."""
    if word_count is None:
        word_count = {}
    if index == len(words):
        return word_count
    word = words[index]
    word_count[word] = word_count.get(word, 0) + 1
    return count_words_recursive(words, index + 1, word_count)


def calculate_similarity(words1, words2):
    """Calculate Jaccard similarity percentage."""
    set1, set2 = set(words1), set(words2)
    if not set1 or not set2:
        return 0.0
    union = set1.union(set2)
    if not union:
        return 0.0
    similarity = (len(set1.intersection(set2)) / len(union)) * 100
    return round(similarity, 2)


def read_file_content(filepath):
    """Read a text file safely."""
    if not os.path.exists(filepath):
        logging.error(f"File not found: {filepath}")
        return None
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        return None


def classify_similarity(similarity):
    """Classify similarity into High/Moderate/Low."""
    if similarity > CONFIG["high_threshold"]:
        return "High Similarity"
    elif similarity > CONFIG["moderate_threshold"]:
        return "Moderate Similarity"
    return "Low Similarity"


def plagiarism_checker(text1, text2):
    """Main plagiarism check between two texts."""
    try:
        words1 = preprocess_text(text1)
        words2 = preprocess_text(text2)
    except ValueError as e:
        logging.error(f"Invalid input: {e}")
        return

    freq1 = count_words_recursive(words1)
    freq2 = count_words_recursive(words2)
    similarity = calculate_similarity(words1, words2)
    classification = classify_similarity(similarity)

    print("\n--- Results ---")
    print(f"Word Frequency Text 1: {freq1}")
    print(f"Word Frequency Text 2: {freq2}")
    print(f"Similarity: {similarity}%")
    print(f"Classification: {classification}")


def main():
    """CLI entry point."""
    print("=== Plagiarism Checker ===")
    print("1. Compare two typed texts")
    print("2. Compare two files")
    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        t1 = input("Enter first text: ")
        t2 = input("Enter second text: ")
        plagiarism_checker(t1, t2)
    elif choice == "2":
        f1 = input("Enter first file path: ")
        f2 = input("Enter second file path: ")
        t1 = read_file_content(f1)
        t2 = read_file_content(f2)
        if t1 and t2:
            plagiarism_checker(t1, t2)
        else:
            print("Could not read one or both files.")
    else:
        print("Invalid choice.")


if _name_ == "_main_":
    main()
