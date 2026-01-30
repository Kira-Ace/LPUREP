
data = ['A', 'X']  
search_term = input("Search for?: ")
j = 0
while j < len(data) and data[j] != search_term:
    j += 1
if j < len(data):
    print(f"Found {search_term} at index {j}")
else:
    print(f"'{search_term}' not found in data")