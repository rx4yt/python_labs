#Write a Python program to add 'ing' at the end of a given string (length should be at 
#least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string 
#length of the given string is less than 3, leave it unchanged.


text = input("Enter a string: ")

if len(text) >= 3:
  if text.endswith('ing'):
    result = text + 'ly'
  else:
    result = text + 'ing'
else:
  result = text

print("Result:", result)