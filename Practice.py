def show_even_numbers(marks):
    even_marks = [m for m in marks if m % 2 == 0]
    print("Even marks:", even_marks)

def show_grades(marks):
    print("\nGrades:")
    for m in marks:
        if m >= 80:
            grade = 'A+'
        elif m >= 70:
            grade = 'A'
        elif m >= 60:
            grade = 'A-'
        elif m >= 50:
            grade = 'B'
        elif m >= 40:
            grade = 'C'
        else:
            grade = 'F'
        print(f"Mark: {m} → Grade: {grade}")

# Main program
marks = list(map(int, input("Enter marks separated by spaces: ").split()))

show_even_numbers(marks)
show_grades(marks)