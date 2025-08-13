import datetime

year = int(input("Enter year:"))

monday = 0

for month in range(1,13):

    dt = datetime.date(year, month, 1)

    if dt.weekday() == 0:
        monday += 1
        print(month)

print("Number of month starting with monday:",monday)

