wanted_book = input()
book = input()
attempts = 0
while book != "No More Books":
    if wanted_book == book:
        break
    attempts += 1
    book = input()
if wanted_book != book:
    print("The book you search is not here!")
    print(f"You checked {attempts} books.")
else:
    print(f"You checked {attempts} books and found it.")
