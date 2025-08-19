import calendar

year = int(input("Enter the year : "))

isLeap = calendar.isleap(year)
if isLeap:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



# calendar.month() 
# calendar.calendar() - full year calendar
# calendar.isleap()
# calendar.weekday(year,month,,day)