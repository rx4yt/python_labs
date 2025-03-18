#11. Check if two lists have at least one common member
def common_member(lst1, lst2):
 return bool(set(lst1) & set(lst2))
print(common_member([1, 2, 3], [4, 5, 3])) # Output: True