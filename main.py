import sys
from stats import count_words, count_character_frequency, sort_character_counts


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

    # Use a relative path here

def main():
    # Check if the right number of arguments were provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Use the provided path from command-line arguments
    book_path = sys.argv[1]

    
    text = get_book_text(book_path)
    
    # Get word count and character frequencies
    word_count = count_words(text)
    char_frequencies = count_character_frequency(text)
    
    # Sort character frequencies
    sorted_chars = sort_character_counts(char_frequencies)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["name"]
        count = char_dict["num"]
        if char.isalpha():  # Skip non-alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()