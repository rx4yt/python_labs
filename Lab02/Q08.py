n = 7  

a, b = 1, 1

print(a, b, end=" ")

for _ in range(n - 2):
    c = a + b  
    print(c, end=" ")
    a, b = b, c  