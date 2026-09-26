# Plagiarism Checker Project
# Author: Utkarsh
# This project compares two text documents and checks for plagiarism
# using simple logic, sets, dictionaries, loops, recursion, and conditionals.

# -------------------------------
# Function to clean and split text
# -------------------------------
def preprocess_text(text):
    """
    Convert text to lowercase and split into words.
    Removes punctuation manually using loops.
    """
    cleaned_text = ""
    for char in text:  # loop through each character
        # keep only alphabets and spaces
        if char.isalpha() or char.isspace():
            cleaned_text += char.lower()
    words = cleaned_text.split()
    return words

# -------------------------------
# Recursive function to count word frequency
# -------------------------------
def count_words_recursive(words, index=0, word_count=None):
    """
    Recursively count word frequency using dictionary.
    """
    if word_count is None:
        word_count = {}

    # base case
    if index == len(words):
        return word_count

    current_word = words[index]
    if current_word in word_count:
        word_count[current_word] += 1
    else:
        word_count[current_word] = 1

    # recursive call
    return count_words_recursive(words, index + 1, word_count)

# -------------------------------
# Function to calculate plagiarism percentage
# -------------------------------
def calculate_similarity(words1, words2):
    """
    Compare two sets of words and calculate similarity percentage.
    """
    set1 = set(words1)
    set2 = set(words2)

    # intersection gives common words
    common_words = set1.intersection(set2)

    # nested conditional logic
    if len(set1) == 0 or len(set2) == 0:
        return 0
    else:
        similarity = (len(common_words) / max(len(set1), len(set2))) * 100
        return similarity

# -------------------------------
# Main function
# -------------------------------
def plagiarism_checker(text1, text2):
    """
    Main function to check plagiarism between two texts.
    """
    # Step 1: Preprocess both texts
    words1 = preprocess_text(text1)
    words2 = preprocess_text(text2)

    # Step 2: Count word frequency using recursion
    freq1 = count_words_recursive(words1)
    freq2 = count_words_recursive(words2)

    # Step 3: Calculate similarity
    similarity_percentage = calculate_similarity(words1, words2)

    # Step 4: Print results with nested conditionals
    print("Word Frequency in Text 1:", freq1)
    print("Word Frequency in Text 2:", freq2)
    print("Similarity Percentage:", similarity_percentage, "%")

    if similarity_percentage > 70:
        print("⚠️ High chance of plagiarism detected!")
    elif similarity_percentage > 40:
        print("⚠️ Moderate similarity, possible plagiarism.")
    else:
        print("✅ Low similarity, plagiarism unlikely.")

# -------------------------------
# Example usage
# -------------------------------
text_a = "Artificial Intelligence is the future of technology."
text_b = "Technology and Artificial Intelligence will shape the future."
plagiarism_checker(text_a, text_b)
print()
print("-"*80)
a_text=input("Enter first text: ")
b_text=input("Enter second text: ")
pragiarism_checker(a_text,b_text)



