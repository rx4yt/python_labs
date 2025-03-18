#Write a Python program to get a string from a given string where all occurrences of its 
#first char have been changed to '$', except the first char itself.


text = input("Enter a string: ")

if len(text) > 1:
 first_char = text[0]
 modified_text = first_char + text[1:].replace(first_char, '$')
else:
 modified_text = text
print("Modified string:", modified_text)