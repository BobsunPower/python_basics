import sys

biggest_number = -sys.maxsize
first_number = int(input())
second_number = int(input())
if first_number > biggest_number:
    biggest_number = first_number
if second_number > biggest_number:
    biggest_number = second_number
print(biggest_number)
