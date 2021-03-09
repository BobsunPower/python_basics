hour = int(input())
minutes = int(input())
time = hour * 60 + minutes + 15
hours = time // 60
minutes = time % 60
if hours >= 24:
    hours -= 24
print(f"{hours}:{minutes:0>2d}")
