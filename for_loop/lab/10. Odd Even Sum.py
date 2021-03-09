numbers = int(input())
odd = 0
even = 0
for n in range(1, numbers + 1):
    number = int(input())
    if n % 2 == 1:
        odd += number
    else:
        even += number
if odd == even:
    print("Yes")
    print(f"Sum = {odd}")
else:
    print("No")
    print(f"Diff = {abs(odd - even)}")
