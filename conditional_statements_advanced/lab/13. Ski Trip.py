days = int(input())
room = input()
opinion = input()
single = 18
apartment = 25
president = 35
nights = days - 1
price = 0
if room == "room for one person":
    price = nights * single
elif room == "apartment":
    price = nights * apartment
    if days < 10:
        price *= 0.7
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.5
elif room == "president apartment":
    price = nights * president
    if days < 10:
        price *= 0.9
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.8
if opinion == "positive":
    price *= 1.25
elif opinion == "negative":
    price *= 0.9
print(f"{price:.2f}")
