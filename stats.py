def count_character_frequency(text):
    """
    Count the frequency of each character in the given text.
    
    Args:
        text (str): The input text to analyze.
    
    Returns:
        dict: A dictionary with lowercase characters as keys 
              and their frequency as values.
    """
    # Convert the text to lowercase to avoid duplicates
    text = text.lower()
    
    # Create a dictionary to store character frequencies
    char_frequency = {}
    
    # Count the frequency of each character
    for char in text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    return char_frequency
def count_words (text: str):
    words = text
    word_count = len(words.split())
    print (f"{word_count} words found in the document")

def count_character_frequency(text):
    # Create a dictionary to store character frequencies
    char_frequency = {}
    
    # Count the frequency of each character (case-insensitive)
    for char in text:
        # Convert to lowercase
        lowercase_char = char.lower()
        
        if lowercase_char in char_frequency:
            char_frequency[lowercase_char] += 1
        else:
            char_frequency[lowercase_char] = 1
    
    return char_frequency
def sort_character_counts(char_counts):
    """
    Sort the character counts in descending order and return a list of dictionaries.
    
    Args:
        char_counts (dict): A dictionary with characters as keys and their counts as values.
    
    Returns:
        list: A list of dictionaries, each containing a character and its count,
              sorted from greatest to least by the count.
    """
    # Sort the dictionary by count (value) in descending order
    sorted_list = [{"name": char, "num": count} for char, count in sorted(char_counts.items(), key=lambda item: item[1], reverse=True)]
    return sorted_list

def count_words(text: str):
    """
    Count the number of words in the given text.
    
    Args:
        text (str): The input text to analyze.
    
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    word_count = len(words)
    
    return word_count

