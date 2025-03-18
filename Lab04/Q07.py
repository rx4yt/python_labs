#WAP to display the smallest word from the string.

text = input("Enter a string: ")
words = text.split()
smallest_word = min(words, key=len)
print("The smallest word is:", smallest_word)