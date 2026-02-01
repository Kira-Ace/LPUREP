n = int(input("What to factor?: "))

def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k
print(list(factors(n)))
    
