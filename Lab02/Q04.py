#4.Write a program to check whether a character is vowel or consonants.

char = input("Enter a character: ").lower()  
vowels = 'aeiou'

if char.isalpha():
    if char in vowels:
        print(char, "is a Vowel")
    else:
        print(char, "is a Consonant")
else:
    print("Invalid input! Please enter a single alphabet character.")