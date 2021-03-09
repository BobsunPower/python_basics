quantity = int(input())
all_numbers = 0
less_than_200 = 0
less_than_400 = 0
less_than_600 = 0
less_than_800 = 0
more_than_800 = 0
for n in range(quantity):
    number = int(input())
    all_numbers += 1
    if number < 200:
        less_than_200 += 1
    elif number < 400:
        less_than_400 += 1
    elif number < 600:
        less_than_600 += 1
    elif number < 800:
        less_than_800 += 1
    else:
        more_than_800 += 1
print(f"{less_than_200 / quantity * 100:.2f}%")
print(f"{less_than_400 / quantity * 100:.2f}%")
print(f"{less_than_600 / quantity * 100:.2f}%")
print(f"{less_than_800 / quantity * 100:.2f}%")
print(f"{more_than_800 / quantity * 100:.2f}%")
