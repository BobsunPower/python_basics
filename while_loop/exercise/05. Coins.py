change = float(input())
cents = change * 100
coins = 0
if cents // 200 > 0:
    coins += cents // 200
    if cents // 200 > 1:
        cents -= 400
    else:
        cents -= 200
if cents // 100 > 0:
    coins += cents // 100
    if cents // 100 > 1:
        cents -= 200
    else:
        cents -= 100
if cents // 50 > 0:
    coins += cents // 50
    if cents // 50 > 1:
        cents -= 100
    else:
        cents -= 50
if cents // 20 > 0:
    coins += cents // 20
    if cents // 20 > 1:
        cents -= 40
    else:
        cents -= 20
if cents // 10 > 0:
    coins += cents // 10
    if cents // 10 > 1:
        cents -= 20
    else:
        cents -= 10
if cents // 5 > 0:
    coins += cents // 5
    if cents // 5 > 1:
        cents -= 10
    else:
        cents -= 5
if cents // 2 > 0:
    coins += cents // 2
    if cents // 2 > 1:
        cents -= 4
    else:
        cents -= 2
if cents // 1 > 0:
    coins += cents // 1
    if cents // 1 > 1:
        cents -= 2
    else:
        cents -= 1
print(int(coins))
