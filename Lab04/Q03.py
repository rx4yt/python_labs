#WAP to check weather a given string is palindrome or not.


text = input("Enter a string: ")

cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
 print(f"'{text}' is a palindrome.")
else:
 print(f"'{text}' is not a palindrome.")