width = int(input())
length = int(input())
height = int(input())
command = input()
space = width * length * height
while command != "Done":
    boxes = int(command)
    space -= boxes
    if space < 0:
        break
    command = input()
if command == "Done":
    print(f"{space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(space)} Cubic meters more.")
