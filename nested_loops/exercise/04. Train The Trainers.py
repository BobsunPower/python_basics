jury = int(input())
total_students = 0
total_grades = 0
while True:
    presentation = input()
    if presentation == "Finish":
        break
    single = 0
    for s in range(jury):
        grade = float(input())
        single += grade
        total_students += 1
        total_grades += grade
    print(f"{presentation} - {single / jury:.2f}.")
print(f"Student's final assessment is {total_grades / total_students:.2f}.")
