operation = input()
total = 0
while operation != "NoMoreMoney":
    money = float(operation)
    if money < 0:
        print("Invalid operation!")
        break
    total += money
    print(f"Increase: {money:.2f}")
    operation = input()
print(f"Total: {total:.2f}")
