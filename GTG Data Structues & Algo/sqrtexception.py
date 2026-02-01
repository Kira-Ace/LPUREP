def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError('must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')

print(sqrt(-5))
print(sqrt(1.0))
print(sqrt("5"))