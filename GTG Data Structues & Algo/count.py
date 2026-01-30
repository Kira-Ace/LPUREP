data = [10, 7, 3, 1, 1, 10, 3, 3, 3]
target = int(input("What to count?: "))

def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n

print(count(data, target))
