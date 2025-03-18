#12. Remove specified elements from a list
def remove_indices(lst, indices):
 return [lst[i] for i in range(len(lst)) if i not in indices]
print(remove_indices(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'], [0, 4, 5])) 
# Output: ['Green', 'White', 'Black']