number = int(input())
letter = int(input())
for first in range(1, number):
    for second in range(1, number):
        for third in range(97, 97 + letter):
            for fourth in range(97, 97 + letter):
                for fifth in range(1, number + 1):
                    chr_third = chr(third)
                    chr_fourth = chr(fourth)
                    if fifth > first and fifth > second:
                        print(f"{first}{second}{chr_third}{chr_fourth}{fifth}", end=" ")
