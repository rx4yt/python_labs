#WAP to accept two strings from the user and display the common words.


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

words1 = set(string1.split())
words2 = set(string2.split())

common_words = words1.intersection(words2)

if common_words:
 print("Common words:", ", ".join(common_words))
else:
 print("No common words found.")