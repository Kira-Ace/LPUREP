data = [1, 5, 7, 10]

big_index = 0
for j in range(len(data)):
    if data[j] > data[big_index]:
        big_index = j
        
print(f"found at index {big_index}")