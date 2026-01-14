def marks_percentage_calculator():
    subjects_input = input("Enter number of subjects: ")
    subjects = int(subjects_input)
    count = 0
    total_marks = 0
    while count < subjects:
        mark_input = input("Enter marks for subject " + str(count + 1) + ": ")
        mark = float(mark_input)
        total_marks = total_marks + mark
        count = count + 1
    max_marks_input = input("Enter total maximum marks: ")
    max_marks = float(max_marks_input)
    percentage = (total_marks / max_marks) * 100
    print("Total Marks Obtained:", total_marks)
    print("Maximum Marks:", max_marks)
    print("Percentage:", percentage)

marks_percentage_calculator()