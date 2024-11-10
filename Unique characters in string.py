def has_unique_characters(input_string):
    # Remove spaces and convert to lowercase
    cleaned_string = input_string.replace(" ", "").lower()

    # Use a set to track seen characters
    seen_characters = set()

    # Iterate over each character in the cleaned string
    for char in cleaned_string:
        if char in seen_characters:
            # If the character is already in the set, return False
            return False
        seen_characters.add(char)
    
    # If no duplicates are found, return True
    return True

# Take input from the user
user_input = input("Enter a string: ")

# Check if the string has unique characters
result = has_unique_characters(user_input)

# Print the result
print(result)
