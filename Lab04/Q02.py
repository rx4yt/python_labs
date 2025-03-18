#WAP to demonstrate built in functions of Strings.

text = " Hello, Python World! "

print("Uppercase:", text.upper())

print("Lowercase:", text.lower())

print("Stripped:", text.strip())

print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

print("Split into words:", text.split())

print("Index of 'Python':", text.find("Python"))

print("Count of 'o':", text.count("o"))

print("Starts with ' Hello':", text.startswith(" Hello"))

print("Ends with 'World! ':", text.endswith("World! "))

alphanumeric_text = "Python123"
print("Is alphanumeric:", alphanumeric_text.isalnum())

print("Is alphabetic:", "Python".isalpha())

digit_text = "12345"
print("Is digit:", digit_text.isdigit())

words = ["Python", "is", "great"]
print("Joined words:", " ".join(words))

print("Length of the string:", len(text))

print("Title Case:", text.title())