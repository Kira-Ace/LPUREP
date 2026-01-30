data = [1, 5, 7, 10]
target = int(input("What target? "))

found = False
for item in data:
    if item == target:
        found = True
        print("found!")
        break
    
if found == False:
    print("not found!")
    
