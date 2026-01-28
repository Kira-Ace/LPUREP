# Legaspi, Jazztinn Kyle G. | CS 101

alist = [1, 3, 5, 7, 9, 11, 13, 15, 4]
if int(input("enter number:")) in alist:
    print("found!")
else:
    print("not here")
    

#return index sequential search (where it is)
def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1
    
anotherlist = [4, 8, 12, 16, 20, 24, 28, 32]
x = int(input("enter number:"))
result = linearSearch(anotherlist, x)

if result != -1:
    print("found at index:", result)
else:
    print("not found!")