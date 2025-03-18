#Write a python program to read a number, if it is an even number , print the square of that number and if it is odd number print cube of that number


num = int(input("Enter a number: "))

if num % 2 == 0:

 result = num ** 2
 print(f"The number is even. The square of {num} is {result}.")
else:

 result = num ** 3
 print(f"The number is odd. The cube of {num} is {result}.")