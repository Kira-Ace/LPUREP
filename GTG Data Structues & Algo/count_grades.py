grades = ['A', 'A', 'A', 'B']
target = input("What grade? ")

def count(grades, target):
    n = 0
    for item in grades:
        if item == target:
            n += 1
    return n

grades.append('A')

prizes = count(grades, target)

print(prizes)
