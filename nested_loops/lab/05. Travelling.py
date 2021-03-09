while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    money = 0
    while money < budget:
        piggy_bank = float(input())
        money += piggy_bank
    print(f"Going to {destination}!")
