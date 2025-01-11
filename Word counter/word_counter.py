# word_counter.py

import string

def clean_text(text):
    """
    Cleans the input text by removing punctuation and converting it to lowercase.
    
    Args:
        text (str): The raw input text.
        
    Returns:
        str: The cleaned text.
    """
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower()

def count_words(text):
    """
    Counts the number of words in the text.
    
    Args:
        text (str): The cleaned input text.
        
    Returns:
        int: The word count.
    """
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Counts the number of characters in the text (excluding spaces).
    
    Args:
        text (str): The cleaned input text.
        
    Returns:
        int: The character count.
    """
    # Remove spaces to count characters only
    return len(text.replace(" ", ""))

def count_sentences(text):
    """
    Counts the number of sentences in the original text.
    Assumes that sentences end with '.', '!', or '?'.
    
    Args:
        text (str): The raw input text.
        
    Returns:
        int: The sentence count.
    """
    sentence_endings = ['.', '!', '?']
    count = 0
    for char in text:
        if char in sentence_endings:
            count += 1
    return count

def main():
    """
    Main function to run the Word Counter application.
    """
    print("=== Word Counter ===")
    print("Enter your text below. When you're done, press Enter on an empty line.")
    
    # Collect multiline input from the user
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    raw_text = "\n".join(lines)
    
    if not raw_text.strip():
        print("No text entered. Exiting the Word Counter.")
        return
    
    # Count sentences before cleaning the text
    sentences = count_sentences(raw_text)
    
    # Clean the text for accurate word and character count
    cleaned_text = clean_text(raw_text)
    
    words = count_words(cleaned_text)
    characters = count_characters(cleaned_text)
    
    print("\n--- Analysis ---")
    print(f"Words: {words}")
    print(f"Characters (excluding spaces): {characters}")
    print(f"Sentences: {sentences}")

if __name__ == "__main__":
    main()