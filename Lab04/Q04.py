#WAP to capitalize the first and last character of each word in a string.


def capitalize_first_last(s):
    words = s.split()
    capitalized_words = []
    
    for word in words:
        if len(word) == 1:
            capitalized_words.append(word.upper())
        else:
            capitalized_words.append(word[0].upper() + word[1:-1] + word[-1].upper())

    return " ".join(capitalized_words)


input_str = input("Enter a string: ")
result = capitalize_first_last(input_str)
print("Output:", result)
