days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
cake_price = 45
waffle_price = 5.8
pancake_price = 3.2
money_per_day = ((cakes * cake_price) + (waffles * waffle_price) + (pancakes * pancake_price)) * bakers
money_before_expenses = money_per_day * days
money_after_expenses = money_before_expenses - (money_before_expenses * 0.125)
print(money_after_expenses)
