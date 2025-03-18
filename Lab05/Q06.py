#Write a Python program to count the number of characters (character frequency) in a string.


text = input("Enter a string: ")

char_frequency = {}

for char in text:
 if char in char_frequency:
   char_frequency[char] += 1
 else:
   char_frequency[char] = 1

print("Character frequency in the string:")
for char, count in char_frequency.items():
 print(f"'{char}': {count}")