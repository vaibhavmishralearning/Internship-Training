import calendar

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))

print("Monthly Calendar : \n")
calendar_display = calendar.month(year,month)
print(calendar_display)



# calendar.month() 
# calendar.calendar() - full year calendar
# calendar.isleap()
# calendar.weekday(year,month,day)