def fibonacci(limit=10):
    a = 0
    b = 1
    count = 0
    while count < limit:
        yield a
        future = a + b
        a = b
        b = future
        count += 1
        
print(list(fibonacci(limit=20)))

print(fibonacci)