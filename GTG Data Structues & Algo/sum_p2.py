import collections

values = [5, 20, 30, 30.0, 10]

def calculate_sum(values):
    if not isinstance(values, collections.abc.Iterable) or isinstance(values, str):
        raise TypeError('parameter must be iterable type')
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('elements must be numeric')
        total = total + v
    return total

print(calculate_sum(values))

#clearer ver: 

"""
def sum(values):
    total = 0
    for v in values:
        total = total + v
    return total"""
    
sum([3.14, "oops"])