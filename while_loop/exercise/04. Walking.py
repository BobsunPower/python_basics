command = input()
goal = 10000
all_steps = 0
while command != "Going home":
    steps = int(command)
    all_steps += steps
    if goal <= all_steps:
        break
    command = input()
if goal > all_steps:
    last_steps = int(input())
    all_steps += last_steps
if goal <= all_steps:
    print("Goal reached! Good job!")
    print(f"{all_steps - goal} steps over the goal!")
else:
    print(f"{goal - all_steps} more steps to reach goal.")
