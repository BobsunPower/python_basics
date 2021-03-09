number = int(input())
for q in range(1, 10):
    for w in range(1, 10):
        for e in range(1, 10):
            for r in range(1, 10):
                if number % q == 0 and number % w == 0 and number % e == 0 and number % r == 0:
                    print(f"{q}{w}{e}{r}", end=" ")
