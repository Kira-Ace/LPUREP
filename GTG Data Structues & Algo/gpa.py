print("""Welcome to the GPA Calculator
Please enter all your letter grades, one per line.
Enter a blank line to designate the end.""")
# map from lettergrade to point value

points = {'A+': 1.0, 'A': 1.0, 'A-': 1.25, 'B+': 1.25, 'B': 1.5, 'B-': 1.75, 'C+': 1.75, 'C': 2.0, 'C-': 2.25, 'D+': 2.25, 'D': 2.75, 'D-': 3.00, 'F': 5.0}

num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print("Unknown grade '{0}' being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]

if num_courses > 0:
    print('Your GPA is {0:.03}'.format(total_points / num_courses))
    