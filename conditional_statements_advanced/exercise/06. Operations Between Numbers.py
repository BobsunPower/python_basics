first_number = int(input())
second_number = int(input())
symbol = input()
result = 0
even_or_odd = ""
if symbol == "+" or symbol == "-" or symbol == "*":
    if symbol == "+":
        result = first_number + second_number
    elif symbol == "-":
        result = first_number - second_number
    elif symbol == "*":
        result = first_number * second_number
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_number} {symbol} {second_number} = {result} - {even_or_odd}")
if symbol == "/" or symbol == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    elif symbol == "/":
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.2f}")
    else:
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result}")
