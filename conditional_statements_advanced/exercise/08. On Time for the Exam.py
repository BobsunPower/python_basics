exam_hours = int(input())
exam_minutes = int(input())
arrive_hours = int(input())
arrive_minutes = int(input())
exam_hours_in_minutes = exam_hours * 60
exam_time = exam_hours_in_minutes + exam_minutes
arrive_hours_in_minutes = arrive_hours * 60
arrive_time = arrive_hours_in_minutes + arrive_minutes
difference = exam_time - arrive_time
difference_hours = 0
difference_minutes = 0
if 0 <= difference <= 30:
    print("On time")
    print(f"{difference} minutes before the start")
elif 30 < difference < 60:
    print("Early")
    print(f"{difference} minutes before the start")
elif difference >= 60:
    difference_hours = difference // 60
    difference_minutes = difference % 60
    print("Early")
    print(f"{difference_hours}:{difference_minutes:0>2d} hours before the start")
elif 0 > difference > -60:
    print("Late")
    print(f"{abs(difference)} minutes after the start")
elif difference <= -60:
    difference_hours = abs(difference) // 60
    difference_minutes = abs(difference) % 60
    print("Late")
    print(f"{abs(difference_hours)}:{abs(difference_minutes):0>2d} hours after the start")
