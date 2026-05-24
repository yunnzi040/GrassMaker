n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Future:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

futures = [Future(date[i], day[i], weather[i]) for i in range(n)]

rain_dates = [i for i in futures if i.weather == "Rain"]

def early_rain_date(dates):
    if len(dates) == 1:
        return dates[0]
    
    early = dates[0]

    for i in dates:
        if i.date < early.date:
            early = i

    return early

result = early_rain_date(rain_dates)
print(result.date, result.day, result.weather)
