name = input()
graduated = False
classes = 1
total = 0
fails = 0
while not graduated:
    grade = float(input())
    if grade >= 4:
        classes += 1
        total += grade
    else:
        fails += 1
    if fails > 1:
        break
    if classes > 12:
        graduated = True
average = total / 12
if fails > 1:
    print(f"{name} has been excluded at {classes} grade")
else:
    print(f"{name} graduated. Average grade: {average:.2f}")
