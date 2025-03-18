#6. Sort list by last element in each tuple
def sort_by_last(tuples):
 return sorted(tuples, key=lambda x: x[-1])
print(sort_by_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])) # Output: [(2, 1), (1,2), (2, 3), (4, 4), (2, 5)]