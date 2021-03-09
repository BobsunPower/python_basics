numbers = int(input())
left = 0
right = 0
for n in range(numbers):
    first = int(input())
    left += first
for n in range(numbers):
    second = int(input())
    right += second
if left == right:
    print(f" Yes, sum = {left}")
else:
    print(f"No, diff = {abs(left - right)}")
