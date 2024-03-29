students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

# Print all students with a count of their courses.
for (name, subjects) in students:
    print(name, "takes", len(subjects), "courses")

# Count how many students are taking CompSci
counter = 0
for (name, subjects) in students:
    for s in subjects:                 # A nested loop!
        if s == "CompSci":
           counter += 1

print("The number of students taking CompSci is", counter)
