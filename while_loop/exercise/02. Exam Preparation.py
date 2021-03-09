limit = int(input())
average = 0
tasks = 0
last_task = ""
fails = 0
while True:
    message = input()
    if message == "Enough":
        break
    grade = int(input())
    average += grade
    tasks += 1
    last_task = message
    if grade <= 4:
        fails += 1
    if fails == limit:
        break
if tasks != 0:
    average /= tasks
if message == "Enough":
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {tasks}")
    print(f"Last problem: {last_task}")
else:
    print(f"You need a break, {limit} poor grades.")
