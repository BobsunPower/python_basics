vacation = float(input())
budget = float(input())
sequence = 0
days = 0
while True:
    if budget >= vacation:
        print(f"You saved the money for {days} days.")
        break
    if sequence > 4:
        print("You can't save the money.")
        print(f"{days}")
        break
    option = input()
    money = float(input())
    days += 1
    if option == "spend":
        sequence += 1
        if money > budget:
            budget = 0
        else:
            budget -= money
    elif option == "save":
        budget += money
        sequence = 0
