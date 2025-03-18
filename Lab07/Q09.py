#9. Write a Python program to find the repeated items of a tuple.  
tuple =(1,4,2,4,5,99,7,17,7,11)

count = 0
for i in range(0, len(tuple)):
    count =tuple.count(tuple[i])
    if count > 1:
     print(tuple[i], "is repeated", count, "times")