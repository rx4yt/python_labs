#4. WAP to demonstrate Pass statements.

def check_number(number):
    if number < 0:
        print("Negative number")
    elif number == 0:
        pass
    else:
      print("Positive number")

check_number(-5)
check_number(0)
check_number(10)