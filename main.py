from collections import Counter

def find_most_common_letters(sentence):
    # Remove spaces from sentence
    sentence = sentence.replace(" ", "")
    # Count characters
    letter_count = Counter(sentence)
    # Get 3 most common characters
    most_common = letter_count.most_common(3)
    # Raise exception if there are less than 3 characters
    if len(most_common) < 3:
        raise Exception("Not enough characters")

    # Return list of characters
    return [letter for letter, count in most_common]

sentence = input("Type a sentence")
most_common_letters = find_most_common_letters(sentence)
print(most_common_letters)