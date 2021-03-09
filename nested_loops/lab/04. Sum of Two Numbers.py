start = int(input())
final = int(input())
n = int(input())
combination = 0
magic = False
for a in range(start, final + 1):
    if magic:
        break
    for b in range(start, final + 1):
        combination += 1
        if a + b == n:
            magic = True
            print(f"Combination N:{combination} ({a} + {b} = {n})")
            break
if not magic:
    print(f"{combination} combinations - neither equals {n}")
