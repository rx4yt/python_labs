#10. Find words longer than n
def words_longer_than(words, n):
 return [word for word in words if len(word) > n]
print(words_longer_than(['hello', 'world', 'python', 'AI'], 4)) # Output: ['hello','world', 'python']