income = float(input())
grade_average = float(input())
minimum_wage = float(input())
social_scholarship = int(minimum_wage * 0.35)
excellent_scholarship = int(grade_average * 25)
if grade_average >= 5.5:
    if income < minimum_wage:
        if excellent_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
        else:
            print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
elif grade_average > 4.5:
    if income < minimum_wage:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You cannot get a scholarship!")
else:
    print(f"You cannot get a scholarship!")
