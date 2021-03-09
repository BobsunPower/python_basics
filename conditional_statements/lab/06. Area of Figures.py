from math import pi
area = 0
figure = input()
if figure == "square":
    a = float(input())
    area = a * a
if figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
if figure == "circle":
    r = float(input())
    area = pi * r ** 2
if figure == "triangle":
    a = float(input())
    h = float(input())
    area = 0.5 * (a * h)
print(f"{area:.3f}")
