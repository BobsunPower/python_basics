quantity = int(input())
all_numbers = 0
divisible_by_two = 0
divisible_by_three = 0
divisible_by_four = 0
for n in range(quantity):
    number = int(input())
    all_numbers += 1
    if number % 2 == 0:
        divisible_by_two += 1
    if number % 3 == 0:
        divisible_by_three += 1
    if number % 4 == 0:
        divisible_by_four += 1
print(f"{divisible_by_two / quantity * 100:.2f}%")
print(f"{divisible_by_three / quantity * 100:.2f}%")
print(f"{divisible_by_four / quantity * 100:.2f}%")
