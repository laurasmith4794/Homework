def isogram(word):
    if type(word) != str:
        raise TypeError('Argument should be a string')
    elif word == "":
        return (word, False)
    else:
        for char in word:
            if word.count(char) > 1:
                return (word, False)
        return (word, True)

if __name__ == '__main__':

    input_word = input("Please enter a word: ")
    print(isogram(input_word))