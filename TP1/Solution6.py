def is_leap(year):
    return((year % 4 == 0 and year % 100 !=0) or year % 400 == 0)

def day_in_month(month, year):
    if month < 1 or month > 12:
        return None
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    return 30  #else 

print()
for y in [1800,1900,2001,2026,2200,2000]:
    if is_leap(y):
        print(y, "is leap year")
    else: print(y, "No")

leap_count = 0
for y in range(2000,2101):
    if is_leap(y):
        leap_count += 1
print("leap year count from 2000 to 2100: ", leap_count)

