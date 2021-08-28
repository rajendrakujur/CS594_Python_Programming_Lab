# Last updated by RAJENDRA KUJUR(214161008) on 18-08-2021 at 20:47
# Python Version: Python 3.9.6
# Editor : Visual Studio Code

# function to check the leap year
# returns true if year is leap else returns false
def isLeapYear(year):
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


# returns day if number is feeded to the function
def numberToDay(number):
    switcher = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    return switcher.get(number)


# returns number of days in a particular month
def daysInMonth(month, year):
    switcher = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if isLeapYear(year) and month > 2:
        return switcher.get(month)+1
    else:
        return switcher.get(month)


# returns which day of the week a date is
def printDayOfWeek(date, month, year):
    # year 1901 is considered as base
    current_day = 1

    # for year traversal
    for _ in range(1901, year):
        if isLeapYear(_):
            current_day += 366
        else:
            current_day += 365
        current_day %= 7

    # for month traversal
    for _ in range(1, month):
        current_day += daysInMonth(_, year)
        current_day %= 7

    # for adding up dates
    current_day += date
    current_day %= 7
    return numberToDay(current_day)


# execution begins
date_of_birth = input(
    "Enter date of birth (>=1901) in dd/mm/yyyy format : ").split('/')
date = int(date_of_birth[0])
month = int(date_of_birth[1])
year = int(date_of_birth[2])
print(printDayOfWeek(date, month, year))
