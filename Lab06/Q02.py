#2. Multiply all the items in a list
def multiply_list(lst):
 result = 1
 for num in lst:
    result *= num
    return result
print(multiply_list([1, 2, 3, 4])) # Output: 24