import string
from collections import Counter

def count_word_frequency(text):
    # Convert text to lowercase and remove punctuation
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation

    # Split the text into words
    words = text.split()

    # Count the frequency of each word using Counter
    word_count = Counter(words)

    # Print each word and its frequency
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Input from the user
text_input = input("Enter a paragraph of text: ")

# Call the function to count word frequency
count_word_frequency(text_input)
