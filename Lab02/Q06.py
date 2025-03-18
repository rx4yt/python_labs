#6.Find the Factorial of a Number.

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0 or num == 1:
    print("The factorial of", num, "is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i 
    print("The factorial of", num, "is", factorial)