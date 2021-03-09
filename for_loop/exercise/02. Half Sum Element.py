import sys

numbers = int(input())
total = 0
maximal = - sys.maxsize
for n in range(numbers):
    number = int(input())
    if number > maximal:
        maximal = number
    total += number
all_numbers = total - maximal
if all_numbers == maximal:
    print("Yes")
    print(f"Sum = {maximal}")
else:
    print("No")
    print(f"Diff = {abs(all_numbers - maximal)}")
