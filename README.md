# Plagiarism Checker

A simple command-line Python program that checks the similarity between two text inputs using basic text preprocessing and word-set comparison.

## Student Details

- Student Name: Utkarsh Kumar Pandey
- Registration Number: 26BAI10231
- Branch: B.Tech – CSE (AI/ML)
- Institution: VIT Bhopal
- Faculty Guide: J. Manikandan
- Course: Python Essentials

## Overview

The Plagiarism Checker is a beginner-friendly Python project that compares two text inputs and calculates their word similarity percentage.

The project demonstrates fundamental Python programming concepts such as:

- Functions
- Conditional statements
- Loops
- Recursion
- Sets
- Dictionaries
- String processing
- User input
- Basic mathematical calculations

## Features

- Accepts two text inputs from the user
- Converts text into lowercase
- Removes non-alphabetic characters
- Extracts words from the text
- Counts words using recursion
- Uses sets to find common words
- Calculates similarity percentage
- Classifies the result into High, Moderate, or Low similarity

## Requirements

- Python 3.x
- No external libraries are required

## How to Run

### 1. Check Python

    python --version

or

    python3 --version

### 2. Clone the Repository

    git clone https://github.com/utkarshpandey431/PLAGIARISM-CHECKER.git
    cd PLAGIARISM-CHECKER

### 3. Run the Program

    python main.py

or

    python3 main.py

## Project Structure

    PLAGIARISM-CHECKER/
    │
    ├── main.py
    ├── README.md
    └── statement.md

## Functional Modules

| Module | Description |
|---|---|
| preprocess_text() | Cleans and normalizes the input text |
| count_words_recursive() | Counts words using recursion |
| calculate_similarity() | Calculates similarity using common word sets |
| plagiarism_checker() | Performs the complete plagiarism checking process |

## Similarity Classification

- High Similarity: More than 70%
- Moderate Similarity: More than 40% and up to 70%
- Low Similarity: 40% or below

## Sample Test Cases

### Test Case 1

Input Text 1: Python is a programming language.

Input Text 2: Python is a programming language.

Expected Result: High Similarity

### Test Case 2

Input Text 1: Python programming is useful.

Input Text 2: Python programming can be useful.

Expected Result: Moderate or High Similarity depending on the calculated percentage.

### Test Case 3

Input Text 1: I like programming.

Input Text 2: The weather is pleasant today.

Expected Result: Low Similarity

## Notes for Evaluators

- The project is implemented using Python only.
- The program does not require external libraries.
- The project demonstrates fundamental Python programming concepts.
- The main program file is main.py.
- The program can be executed directly from the command line.
- The similarity calculation is based on common words between the two texts.
- This is an educational project and is intended to demonstrate basic Python programming concepts.

## Author

Utkarsh Kumar Pandey

## Faculty Guide

J. Manikandan
