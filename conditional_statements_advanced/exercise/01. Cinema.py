premiere = 12
normal = 7.5
discount = 5
income = 0
movie = input()
rows = int(input())
columns = int(input())
capacity = rows * columns
if movie == "Premiere":
    income = capacity * 12
elif movie == "Normal":
    income = capacity * 7.5
elif movie == "Discount":
    income = capacity * 5
print(f"{income:.2f}")
