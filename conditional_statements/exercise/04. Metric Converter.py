number = float(input())
unit = input()
converted = input()
if unit == "m":
    number *= 1000
elif unit == "cm":
    number *= 10
if converted == "m":
    number /= 1000
elif converted == "cm":
    number /= 10
print(f"{number:.3f}")
