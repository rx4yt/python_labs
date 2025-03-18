#10. Write a Python program to check whether an element exists within a tuple.  
tuple =(1,4,2,4,5,99,7,17,7,11)

for i in range(0, len(tuple)):
    if tuple[i] == 7:
          print("7 found at index: ", i)
    else:
      print("7 not found at index: ", i)