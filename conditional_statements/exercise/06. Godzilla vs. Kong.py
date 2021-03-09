budget = float(input())
extra = int(input())
single_costume = float(input())
decor = budget * 0.1
clothing = extra * single_costume
if extra > 150:
    clothing *= 0.9
expenses = decor + clothing
total = abs(budget - expenses)
if budget >= expenses:
    print("Action!")
    print(f"Wingard starts filming with {total:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total:.2f} leva more.")
