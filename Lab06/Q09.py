#9. Clone or copy a list
def clone_list(lst):
 return lst[:]
original = [1, 2, 3]
copy = clone_list(original)
print(copy) # Output: [1, 2, 3]