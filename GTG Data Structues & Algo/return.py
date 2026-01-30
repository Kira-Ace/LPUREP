
data = [1, 2, 6, 8, 10]
target = input("What target? ")

def contains(data, target):
    for item in data:
        if item == int(target):
            return True
    return False
    
if contains(data, target):
    print("Found!")
else:
    print("Not found!")