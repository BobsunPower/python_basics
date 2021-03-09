total = int(input())
number = 1
enough = False
for r in range(1, total + 1):
    for c in range(1, r + 1):
        if number > total:
            enough = True
            break
        print(f"{number} ", end="")
        number += 1
    if enough:
        break
    print()
