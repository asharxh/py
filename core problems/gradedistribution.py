print("=== Grade Distribution System ===.\n")

grades_input = input("Enter students' numeric grades separated by spaces: ")

grades = [int(x) for x in grades_input.split()]

distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

for grade in grades:
    if 90 <= grade <= 100:
        distribution['A'] += 1
    elif 80 <= grade < 90:
        distribution['B'] += 1
    elif 70 <= grade < 80:
        distribution['C'] += 1
    elif 60 <= grade < 70:
        distribution['D'] += 1
    else:
        distribution['F'] += 1

print("\nGrade Distribution:")
for grade, count in distribution.items():
    print(f"{grade}: {count}")

total_students = len(grades)
print("\nPercentage Distribution:")
for grade, count in distribution.items():
    percent = (count / total_students) * 100
    print(f"{grade}: {percent:.1f}%")