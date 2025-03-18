#5.Write a program to find the smallest of two numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 < num2:
    print("The smallest number is:", num1)
elif num2 < num1:
    print("The smallest number is:", num2)
else:
    print("Both numbers are equal.")