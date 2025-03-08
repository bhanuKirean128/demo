import string
from collections import Counter


def preprocess_text(text):
    """Preprocess the text by converting to lowercase and removing punctuation."""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def find_repeated_keywords(filename):
    """Find repeated keywords in the provided text file."""
    try:
        with open(filename, 'r') as file:
            text = file.read()

        # Preprocess the text
        text = preprocess_text(text)

        # Split the text into words
        words = text.split()

        # Count the frequency of each word
        word_counts = Counter(words)

        # Filter words that appear more than once
        repeated_keywords = {word: count for word, count in word_counts.items() if count > 1}

        return repeated_keywords

    except FileNotFoundError:
        print("The specified file was not found.")
        return {}


def main():
    # Hardcoded file name
    filename = "repeat.txt"  # Specify the filename here

    repeated_keywords = find_repeated_keywords(filename)

    if repeated_keywords:
        print("Repeated keywords and their frequencies:")
        for word, count in repeated_keywords.items():
            print(f"{word}: {count}")
    else:
        print("No repeated keywords found.")


# Run the program
if __name__ == "__main__":
    main()
