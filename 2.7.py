def enter_marks():
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)
    return marks


def calculate_percentage(marks):
    return sum(marks) / len(marks)


def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


# Menu Driven
while True:
    print("""
1. Enter Marks
2. Calculate Percentage
3. Assign Grade
4. Exit
""")

    choice = int(input("Enter choice: "))

    if choice == 1:
        marks = enter_marks()

    elif choice == 2:
        if 'marks' in locals():
            percentage = calculate_percentage(marks)
            print("Percentage:", percentage)
        else:
            print("Enter marks first.")

    elif choice == 3:
        if 'marks' in locals():
            percentage = calculate_percentage(marks)
            grade = assign_grade(percentage)
            print("Grade:", grade)
        else:
            print("Enter marks first.")

    elif choice == 4:
        break

    else:
        print("Invalid choice")
