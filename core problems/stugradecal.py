def gradecal():
    subjects = int(input("Enter total number of Subjects: "))
    marks = []
    for i in range(subjects):
        score = float(input(f"Enter marks for subjects {i+1}:"))
        marks.append(score)
        
    total = sum(marks)
    average = total/subjects
    
    if average >= 90:
        grade = "A"
    elif average >=75:
        grade="B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"
        
    print("\n---- Result---")
    print("Total Marks", total)
    print("Average marks: ", average)
    print("Grade: ", grade)
    
gradecal()