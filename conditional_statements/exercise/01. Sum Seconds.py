first = int(input())
second = int(input())
third = int(input())
total = first + second + third
minutes = total // 60
seconds = total % 60
print(f"{minutes}:{seconds:0>2d}")
