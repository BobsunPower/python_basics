age = int(input())
washer = float(input())
toys_price = int(input())
toys = 0
piggy_bank = 0
money = 10
for a in range(1, age + 1):
    if a % 2 == 1:
        toys += 1
    else:
        piggy_bank += money
        piggy_bank -= 1
        money += 10
toys *= toys_price
piggy_bank += toys
if piggy_bank >= washer:
    print(f"Yes! {piggy_bank - washer:.2f}")
else:
    print(f"No! {washer - piggy_bank:.2f}")
