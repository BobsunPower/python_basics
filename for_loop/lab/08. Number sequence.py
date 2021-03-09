import sys

numbers = int(input())
minimal = sys.maxsize
maximal = - sys.maxsize
for n in range(numbers):
    number = int(input())
    if number < minimal:
        minimal = number
    if number > maximal:
        maximal = number
print(f"Max number: {maximal}")
print(f"Min number: {minimal}")
