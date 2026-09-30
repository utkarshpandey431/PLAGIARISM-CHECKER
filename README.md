# Plagiarism Checker

A simple command-line Python program that compares two text documents and calculates the similarity percentage to detect possible plagiarism.

*Student:* Utkarsh Kumar Pandey  
*Registration No.:* 26BAI10231  
*Branch:* CSE (AI/ML)  
*Institution:* VIT Bhopal  
*Faculty Guide:* J. Manikandan  
*Course:* Python Essentials – Evaluated Course Project  

---

## Overview

This project takes two text inputs, cleans them, counts word frequencies using recursion, calculates similarity using set intersection, and classifies the result as High, Moderate, or Low similarity.

It uses only core Python concepts: loops, conditionals, functions, recursion, sets, and dictionaries. No external libraries are required.

---

## Features

- Text preprocessing (lowercase and punctuation removal)
- Recursive word-frequency counting
- Similarity calculation using sets
- Clear similarity verdict (High / Moderate / Low)
- Built-in demo and interactive mode

---

## Requirements

- Python 3.6 or higher
- No additional packages needed

---

## How to Run

### 1. Check Python

bash
python --version


or

bash
python3 --version


### 2. Clone the Repository

bash
git clone https://github.com/utkarshpandey431/PLAGIARISM-CHECKER.git
cd PLAGIARISM-CHECKER


### 3. Run the Program

bash
python main.py


or

bash
python3 main.py


---

## Project Structure

text
PLAGIARISM-CHECKER/
├── main.py
├── README.md
└── statement.md


---

## Functional Modules

| Module | Function | Purpose |
|---|---|---|
| 1 | preprocess_text() | Cleans text and splits it into words |
| 2 | count_words_recursive() | Counts word frequency using recursion |
| 3 | calculate_similarity() | Calculates similarity percentage using sets |
| 4 | plagiarism_checker() | Main driver function |

---

## Sample Test Cases

### Test 1 – Moderate Similarity

*Text 1:*  
Artificial Intelligence is the future of technology.

*Text 2:*  
Technology and Artificial Intelligence will shape the future.

*Expected:* Around 50–65% → Moderate similarity

---

### Test 2 – High Similarity

*Text 1:*  
Python is a powerful programming language.

*Text 2:*  
Python is a powerful programming language used widely.

*Expected:* More than 70% → High similarity

---

### Test 3 – Low Similarity

*Text 1:*  
The sun rises in the east.

*Text 2:*  
Computers process data very quickly.

*Expected:* Near 0% → Low similarity

---

## Notes for Evaluators

- Fully executable from the command line
- No GUI required
- No external packages to install
- Works on Windows, macOS, and Linux

---

*Author:* Utkarsh Kumar Pandey (26BAI10231)  
*Faculty:* J. Manikandan | VIT Bhopal | CSE (AI/ML)
