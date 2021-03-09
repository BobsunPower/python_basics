year = input()
holidays = int(input())
hometown = int(input())
weekends = 48
sofia = weekends - hometown
sofia_games = sofia * 0.75
hometown_games = hometown
holiday_games = holidays * (2/3)
total = sofia_games + hometown_games + holiday_games
if year == "leap":
    total *= 1.15
print(int(total))
