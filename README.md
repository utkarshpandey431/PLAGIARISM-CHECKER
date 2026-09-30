# Plagiarism Checker

A command-line Python application that compares two text inputs and calculates similarity using Jaccard similarity on word sets.

## Student Details

- *Name:* Utkarsh Kumar Pandey
- *Registration Number:* 26BAI10231
- *Branch:* B.Tech – CSE (AI/ML)
- *Institution:* VIT Bhopal
- *Faculty Guide:* J. Manikandan
- *Course:* Python Essentials

## Overview

This project compares two text inputs (typed or read from files) and calculates a similarity percentage using text preprocessing, recursive word counting, and Jaccard similarity. Results are classified as High, Moderate, or Low similarity.

## Features

- Accepts text input via console or file
- Cleans and normalizes text (lowercase, remove non-alphabetic characters)
- Counts word frequency using recursion
- Calculates Jaccard similarity percentage
- Classifies result into High / Moderate / Low
- Error handling for missing files and invalid input
- Configurable thresholds via config.json

## Technologies Used

- Python 3.x
- Standard Library: json, os, logging, unittest

## Project Structure


PLAGIARISM-CHECKER/
│
├── main.py              # Main program
├── test_main.py         # Unit tests
├── config.json          # Threshold configuration
├── requirements.txt     # Dependencies
├── README.md            # Documentation
├── statement.md         # Problem statement
└── data/
    ├── sample1.txt      # Sample text 1
    └── sample2.txt      # Sample text 2


## Installation & Run

### 1. Check Python

bash
python --version


### 2. Clone Repository

bash
git clone https://github.com/utkarshpandey431/PLAGIARISM-CHECKER.git
cd PLAGIARISM-CHECKER


### 3. Run Program

bash
python main.py


### 4. Run Tests

bash
python -m unittest test_main.py


## Functional Modules

| Module | Description |
|---|---|
| preprocess_text() | Cleans and normalizes text |
| count_words_recursive() | Recursive word frequency counter |
| calculate_similarity() | Jaccard similarity calculator |
| classify_similarity() | Classifies similarity level |
| read_file_content() | File reader with error handling |
| plagiarism_checker() | Orchestrates full check |
| main() | CLI interface |

## Similarity Classification

- *High:* > 70%
- *Moderate:* > 40% and ≤ 70%
- *Low:* ≤ 40%

## Sample Test Cases

| Case | Text 1 | Text 2 | Expected |
|---|---|---|---|
| 1 | "Python is a programming language" | "Python is a programming language" | High (100%) |
| 2 | "Python programming is useful" | "Python programming can be useful" | Moderate (~50%) |
| 3 | "I like programming" | "The weather is pleasant today" | Low (0%) |

## Notes for Evaluators

- Runs fully from the command line
- No external libraries required
- Repository is public
- Main file: main.py

## Author

Utkarsh Kumar Pandey

## Faculty Guide

J. Manikandan
