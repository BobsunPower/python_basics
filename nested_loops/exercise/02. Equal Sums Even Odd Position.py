minimal = int(input())
maximal = int(input())
for number in range(minimal, maximal + 1):
    string_number = str(number)
    even = 0
    odd = 0
    for index, digit in enumerate(string_number):
        if index % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
    if even == odd:
        print(number, end=" ")
