month = input()
nights = int(input())
studio_per_night = 0
apartment_per_night = 0
studio_total = 0
apartment_total = 0
if month == "May" or month == "October":
    studio_per_night = 50
    apartment_per_night = 65
    studio_total = studio_per_night * nights
    apartment_total = apartment_per_night * nights
    if nights > 14:
        studio_total *= 0.7
    elif nights > 7:
        studio_total *= 0.95
elif month == "June" or month == "September":
    studio_per_night = 75.2
    apartment_per_night = 68.7
    studio_total = studio_per_night * nights
    apartment_total = apartment_per_night * nights
    if nights > 14:
        studio_total *= 0.8
elif month == "July" or month == "August":
    studio_per_night = 76
    apartment_per_night = 77
    studio_total = studio_per_night * nights
    apartment_total = apartment_per_night * nights
if nights > 14:
    apartment_total *= 0.9
print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")
