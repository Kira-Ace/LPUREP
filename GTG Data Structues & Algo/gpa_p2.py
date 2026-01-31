print("""Welcome to the GPA Calculator
Please enter all your letter grades in a list using commas.
Press Enter to print your average.""")
# map from lettergrade to point value
points = {'A+': 1.0, 'A': 1.0, 'A-': 1.25, 'B+': 1.25, 'B': 1.5, 'B-': 1.75, 'C+': 1.75, 'C': 2.0, 'C-': 2.25, 'D+': 2.25, 'D': 2.75, 'D-': 3.00, 'F': 5.0}


def compute_gpa(grade, points = {'A+': 1.0, 'A': 1.0, 'A-': 1.25, 'B+': 1.25, 'B': 1.5, 'B-': 1.75, 'C+': 1.75, 'C': 2.0, 'C-': 2.25, 'D+': 2.25, 'D': 2.75, 'D-': 3.00, 'F': 5.0}):
    num_courses = 0
    total_points = 0
    for g in grade:
        if g in points:
            num_courses += 1
            total_points += points[g]    
            
    return total_points/num_courses 

grade = input("What grades?: ")
print(compute_gpa(grade))


    
    


    

