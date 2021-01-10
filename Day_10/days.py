def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year_i, month_i):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_i < 1 or month_i > 12:
        return "Invalid month entered."
    leap = is_leap(year_i)
    if month_i == 2 and leap == True:
        return 29
    return month_days[month_i-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)