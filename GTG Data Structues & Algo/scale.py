data = [6, 2, 9, 10]
factor = int(input("What factor?: "))

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
    return data
        
print(scale(data, factor))

