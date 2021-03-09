prime = 0
non_prime = 0
while True:
    enter = input()
    if enter == "stop":
        break
    is_prime = True
    number = int(enter)
    if number < 0:
        print("Number is negative.")
        continue
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
            break
    if is_prime:
        prime += number
    else:
        non_prime += number
print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
