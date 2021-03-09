record = float(input())
distance = float(input())
time = float(input())
seconds = distance * time
delay = int(distance / 15) * 12.5
total = seconds + delay
if total < record:
    print(f" Yes, he succeeded! The new world record is {total:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(total - record):.2f} seconds slower.")
