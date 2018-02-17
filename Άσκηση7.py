import calendar
import datetime

now = datetime.datetime.now()
xronia = now.year
mera = now.day
mhnas = now.month
sumdays = 0
baseweekday = calendar.weekday(xronia, mhnas, mera)
y = mhnas
v = ""
if baseweekday == 0:
    v = "Monday"
if baseweekday == 1:
    v = "Tuesday"
if baseweekday == 2:
    v = "Wednesday"
if baseweekday == 3:
    v = "Thursday"
if baseweekday == 4:
    v = "Friday"
if baseweekday == 5:
    v = "Saturday"
if baseweekday == 6:
    v = "Sunday"
for x in range(0, 11):
    while y < 13:
        if datetime.datetime(xronia, y, mera).weekday() == baseweekday:
            sumdays = sumdays + 1
            print(v, "the", mera, "||", "Year:", xronia, "Month:", y)
        y = y + 1
    xronia = xronia + 1
    y = 1
print("Total", v, "the", mera, ":", sumdays)
