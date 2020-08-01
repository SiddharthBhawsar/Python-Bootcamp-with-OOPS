import datetime
schedule={"Monday":"GymDay","Tuesday":"YogaDay", "Wednesday":"TempleDay", "Thursday":"GymDay", "Friday":"Yogaday","Saturday":"TempleDay"}
day=datetime.datetime.today().strftime("%A")
# print(day)

for item in schedule.keys():
    if day==item:
        print(f"Today day is {day}, which means {schedule[item]}")