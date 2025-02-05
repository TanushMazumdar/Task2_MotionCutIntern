def count_words(text):
    """
    Function to count the number of words in a given text.
    A word is defined as a sequence of characters separated by whitespace.
    """
    words = text.split()  # Splitting the text into words based on spaces
    return len(words)  # Returning the word count


def main():
    """
    Main function to handle user input and display output.
    """
    print("Welcome to the Word Counter Program!")
    user_input = input("Please enter a sentence or paragraph: ")
    
    if not user_input.strip():  # Checking for empty input
        print("Error: Input cannot be empty. Please enter some text.")
    else:
        word_count = count_words(user_input)  # Counting words
        print(f"Word Count: {word_count}")  # Displaying the result


if __name__ == "__main__":
    main()
