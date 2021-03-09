length = int(input())
width = int(input())
height = int(input())
space_used_percentage = float(input())
volume = length * width * height
water_capacity = volume * 0.001
space_used_percentage *= 0.01
liters = water_capacity * (1 - space_used_percentage)
print(liters)
