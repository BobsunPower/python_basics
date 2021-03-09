budget = int(input())
season = input()
fishermen = int(input())
boat = 0
total = 0
if season == "Spring":
    boat = 3000
    if fishermen <= 6:
        boat *= 0.9
    elif fishermen <= 11:
        boat *= 0.85
    else:
        boat *= 0.75
elif season == "Summer" or season == "Autumn":
    boat = 4200
    if fishermen <= 6:
        boat *= 0.9
    elif fishermen <= 11:
        boat *= 0.85
    else:
        boat *= 0.75
elif season == "Winter":
    boat = 2600
    if fishermen <= 6:
        boat *= 0.9
    elif fishermen <= 11:
        boat *= 0.85
    else:
        boat *= 0.75
if season != "Autumn" and fishermen % 2 == 0:
    boat *= 0.95
if budget >= boat:
    print(f"Yes! You have {abs(budget - boat):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - boat):.2f} leva.")
