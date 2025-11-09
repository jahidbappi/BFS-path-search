marks = []
n = int(input('Total input: '))

for i in range(n):
    x = int(input('Enter the numbers: '))
    marks.append(x)


def show_even_marks(marks):
    even_marks = [m for m in marks if m % 2 == 0]
    print("Even marks:", even_marks)


def show_grades(marks):
    print("Grades:")
    for m in marks:
        if m >= 90:
            grade = 'A+'
        elif m >= 85:
            grade = 'A'
        elif m >= 80:
            grade = 'B+'
        elif m >= 75:
            grade = 'B'
        elif m >= 50:
            grade = 'D'
        else:
            grade = 'F'
        print(f"Mark: {m} → Grade: {grade}")


show_even_marks(marks)
show_grades(marks)