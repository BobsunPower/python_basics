total = 0
student = 0
standard = 0
kid = 0
while True:
    movie = input()
    if movie == "Finish":
        print(f"Total tickets: {total}")
        print(f"{student / total * 100:.2f}% student tickets.")
        print(f"{standard / total * 100:.2f}% standard tickets.")
        print(f"{kid / total * 100:.2f}% kids tickets.")
        break
    seats = int(input())
    sold = 0
    while True:
        ticket = input()
        if ticket == "End":
            break
        total += 1
        sold += 1
        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1
        if sold == seats:
            break
    print(f"{movie} - {sold / seats * 100:.2f}% full.")
