width = int(input())
length = int(input())
cake = width * length
action = ""
while cake > 0:
    action = input()
    if action == "STOP":
        print(f"{cake} pieces are left.")
        break
    pieces = int(action)
    cake -= pieces
if action != "STOP":
    print(f"No more cake left! You need {abs(cake)} pieces more.")
