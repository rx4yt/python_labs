num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2:
 print(f"The common number is: {num1}")
elif num1 == num3:
 print(f"The common number is: {num1}")
elif num2 == num3:
 print(f"The common number is: {num2}")
else:
 print("No two numbers are equal.")