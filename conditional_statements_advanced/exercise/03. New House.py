flowers = input()
quantity = int(input())
budget = int(input())
rose = 5
dahlia = 3.8
tulip = 2.8
narcissus = 3
gladiolus = 2.5
total = 0
if flowers == "Roses":
    total = rose * quantity
    if quantity > 80:
        total *= 0.9
elif flowers == "Dahlias":
    total = dahlia * quantity
    if quantity > 90:
        total *= 0.85
elif flowers == "Tulips":
    total = tulip * quantity
    if quantity > 80:
        total *= 0.85
elif flowers == "Narcissus":
    total = narcissus * quantity
    if quantity < 120:
        total *= 1.15
elif flowers == "Gladiolus":
    total = gladiolus * quantity
    if quantity < 80:
        total *= 1.2
if budget >= total:
    print(f"Hey, you have a great garden with {quantity} {flowers} and {abs(budget - total):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - total):.2f} leva more.")
