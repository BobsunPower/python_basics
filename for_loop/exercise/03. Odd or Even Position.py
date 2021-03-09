import sys

quantity = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = - sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = - sys.maxsize

for n in range(1, quantity + 1):
    number = float(input())
    if n % 2 == 1:
        odd_sum += number
        if number < odd_min:
            odd_min = number
        if number > odd_max:
            odd_max = number
    else:
        even_sum += number
        if number < even_min:
            even_min = number
        if number > even_max:
            even_max = number
print(f"OddSum={odd_sum:.2f},")
if odd_min != sys.maxsize and odd_max != - sys.maxsize:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMin=No,")
    print("OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_min != sys.maxsize and even_max != - sys.maxsize:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMin=No,")
    print("EvenMax=No")
