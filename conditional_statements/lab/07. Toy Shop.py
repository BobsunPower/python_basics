puzzle_price = 2.6
doll_price = 3
bear_price = 4.1
minion_price = 8.2
truck_price = 2

holiday_price = float(input())
puzzle_quantity = int(input())
doll_quantity = int(input())
bear_quantity = int(input())
minion_quantity = int(input())
truck_quantity = int(input())

money = (puzzle_quantity * puzzle_price) + (doll_quantity * doll_price) + (bear_quantity * bear_price) + (
        minion_quantity * minion_price) + (truck_quantity * truck_price)
toys = puzzle_quantity + doll_quantity + bear_quantity + minion_quantity + truck_quantity
if toys >= 50:
    money *= 0.75
rent = money * 0.1
profit = money - rent

total = abs(holiday_price - profit)
if profit >= holiday_price:
    print(f"Yes! {total:.2f} lv left.")
else:
    print(f"Not enough money! {total:.2f} lv needed.")
